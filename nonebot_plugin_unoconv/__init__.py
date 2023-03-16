import nonebot
from nonebot import on_command, on_notice, logger
from nonebot.adapters.onebot.v11.bot import Bot
from nonebot.adapters.onebot.v11.event import NoticeEvent, MessageEvent, GroupMessageEvent,Event, GroupUploadNoticeEvent
from nonebot.adapters.onebot.v11.message import MessageSegment, Message
from nonebot.typing import T_State
from nonebot.params import CommandArg

import os
from .install import linux_install
from .unoconv import download, convert_to_pdf, del_file, check_type

linux_install("unoconv")


queue = {}


to_pdf_f = on_command('强制文件转换')
@to_pdf_f.handle()
async def _(bot: Bot, event: MessageEvent, state: T_State, export: Message = CommandArg()):

    if str(export) != '':
        state['output_type'] = export

@to_pdf_f.got('output_type', '请输入转换格式:')
async def _(bot: Bot, event: MessageEvent, state: T_State):

    queue[event.user_id] = {'farce':1}
    queue[event.user_id]['output_type'] = str(state['output_type']).lower()
    await bot.send(event, message='准备完毕, 请发文档')


to_pdf = on_command('文件转换')
@to_pdf.handle()
async def _(bot: Bot, event: MessageEvent, state: T_State, export: Message = CommandArg()):

    if str(export) != '':
        state['output_type'] = export
    

@to_pdf.got('output_type', '请输入转换格式:')
async def _(bot: Bot, event: MessageEvent, state: T_State):

    queue[event.user_id] = {}
    queue[event.user_id]['output_type'] = str(state['output_type']).lower()
    await bot.send(event, message='准备完毕, 请发文档')


notice = on_notice()
@notice.handle()
async def _(bot: Bot, event: NoticeEvent):
    
    if not queue.get(event.user_id, None):
        return
    
    if not queue[event.user_id].get('farce'):
        if not check_type('output', queue[event.user_id]['output_type']):
            await bot.finish(message='不支持该输出格式')

    try:
        if event.notice_type == 'group_upload':
            name = event.file.name 
            url = event.file.url
        elif event.notice_type == 'offline_file':
            name = event.file['name'] 
            url = event.file['url']
        await conver_and_upload(bot, event, queue[event.user_id]['output_type'], url, name)
    except Exception as e:
        await bot.finish(message='发生错误')
        logger.error(e.__repr__)
    del(queue[event.user_id])


async def conver_and_upload(bot: Bot, event: Event, export_type: str, url: str, name: str):

    logger.info('准备下载文件')
    
    if  not check_type('input' ,name.split('.')[-1]):
        await bot.finish(message='错误的输入格式')
        

    raw_file = await download(url, name)    

    if not os.path.exists(raw_file):
        await bot.finish(message='下载失败')

    file = await convert_to_pdf(export_type, raw_file)

    name = file.split('/')[-1]
    if isinstance(event, GroupMessageEvent) or isinstance(event, GroupUploadNoticeEvent):
        await bot.call_api('upload_group_file', group_id= event.group_id, name=name, file=file)
    else:
        await bot.call_api('upload_private_file', user_id= event.user_id, name=name, file=file)

    await  del_file(file)
