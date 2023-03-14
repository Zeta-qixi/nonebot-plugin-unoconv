import subprocess
import asyncio
import os


CHECK = {
    # http://dag.wiee.rs/home-made/unoconv/
    'output': ['pdf', 'html', 'doc'],
    'input' : ['docx', 'doc', 'odt'],
}

PATH = os.path.dirname(os.path.abspath(__file__))

def check_type( f, type_ ):
    return type_ in CHECK[f]



async def download(url, name):

    path = PATH + '/' + name
    await run_subprocess(["curl", "-o", path,  url])
    return path


async def convert_to_pdf(export_type, filePath):
    
    fileName, _ = os.path.splitext(filePath)
    outPath = fileName + "." + export_type
    await run_subprocess(["unoconv", "-f", export_type, "-o", outPath, filePath])
    await del_file(filePath)
    return outPath


async def del_file(filePath):
    if  os.path.exists(filePath):
        await run_subprocess(["rm", filePath, '-f'])


async def run_subprocess(args):

    process = await asyncio.create_subprocess_exec(*args)
    await process.communicate()


# example usage
# outPath = convert_to_pdf("pdf","raw/1.docx")

