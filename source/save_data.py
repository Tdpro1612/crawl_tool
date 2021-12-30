from typing import *
import jsbeautifier
import codecs
import json

def write_csv(file_path: Text, dict_info: Union[List, Dict]) -> None:
    """
    Write the content from dictionary into file with a beautiful format

    Args:
        file_path (Text): The file path
        dict_info (Dict): Dict will be dump

    Returns:

    """
    dict_info.to_csv(file_path, index = False)

def write_excel(file_path: Text, dict_info: Union[List, Dict],parameter) -> None:
    """
    Write the content from dictionary into file with a beautiful format

    Args:
        file_path (Text): The file path
        dict_info (Dict): Dict will be dump
        parameter :  index = False
    Returns:

    """
    dict_info.to_excel(file_path,parameter)

def write_txt(file_path: Text, dict_info: Union[List, Dict],parameter) -> None:
    """
    Write the content from dictionary into file with a beautiful format

    Args:
        file_path (Text): The file path
        dict_info (Dict): Dict will be dump
        parameter : sep=":",columns=None,header=False,index=False
    Returns:

    """
    dict_info.to_csv(file_path,parameter)

def write_json_beautifier(file_path: Text, dict_info: Union[List, Dict]) -> None:
    """
    Write the content from dictionary into file with a beautiful format

    Args:
        file_path (Text): The file path
        dict_info (Dict): Dict will be dump

    Returns:

    """
    opts = jsbeautifier.default_options()
    opts.indent_size = 4
    dict_ = jsbeautifier.beautify(json.dumps(dict_info, ensure_ascii=False), opts)
    with codecs.open(file_path, 'w', 'utf-8') as f:
        f.write(dict_)