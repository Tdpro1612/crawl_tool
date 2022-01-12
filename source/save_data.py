from typing import *
import jsbeautifier
import codecs
import json
import pandas as pd


def write_csv(file_path: Text, dict_info: Union[List, Dict],columns,*args):
    """
    Write the content from dictionary into file with a beautiful format

    Args:
        file_path (Text): The file path
        dict_info (Dict): Dict will be dump
        param : index=False
    Returns:

    """
    df = pd.DataFrame(dict_info,columns=columns)  
    df.to_csv(file_path,index=False)

def write_excel(file_path: Text, dict_info: Union[List, Dict],columns,*args):
    """
    Write the content from dictionary into file with a beautiful format

    Args:
        file_path (Text): The file path
        dict_info (Dict): Dict will be dump
        parameter :  index = False
    Returns:

    """
    df = pd.DataFrame(dict_info,columns=columns)  
    df.to_excel(file_path,index=False)

def write_txt(file_path: Text, dict_info: Union[List, Dict],columns,*args):
    """
    Write the content from dictionary into file with a beautiful format

    Args:
        file_path (Text): The file path
        dict_info (Dict): Dict will be dump
        parameter : sep=":",columns=None,header=False,index=False
    Returns:

    """
    df = pd.DataFrame(dict_info,columns=columns)  
    df.to_csv(file_path,index=False)

def write_json_beautifier(file_path: Text, dict_info: Union[List, Dict],ensure_ascii=False,*args):
    """
    Write the content from dictionary into file with a beautiful format

    Args:
        file_path (Text): The file path
        dict_info (Dict): Dict will be dump
        default :  ensure_ascii=False
    Returns:

    """
    opts = jsbeautifier.default_options()
    opts.indent_size = 4
    dict_ = jsbeautifier.beautify(json.dumps(dict_info,ensure_ascii=False,*args), opts)
    with codecs.open(file_path, 'w', 'utf-8') as f:
        f.write(dict_)

