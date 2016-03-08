"""Simple and Fast Python Compiler .py to .pyc (ByteCode) - Version 0.0.1.

Author: Edson Lourenço
E-mail: edson.lourenco@outlook.com
Version: 0.0.1
Platform: any
Date Creation: 2016-03-07 at 13:00

"""
# -*- coding: utf-8 -*-


class Compiler(object):
    """Compiler Class."""

    def ToCompileAllFiles(self, pDirProject):
        """Compile all folder projeect."""
        import re
        import compileall
        import os.path
        if pDirProject != "":
            if "," not in pDirProject:
                try:
                    rexp = re.compile(r'[/\\][.]svn')
                    normalpath = os.path.normpath(pDirProject)
                    compileall.compile_dir(normalpath,
                                           rx=rexp, force=True,
                                           optimize=2)
                    normalpath = os.path.join(normalpath, "_pycache_")
                    print("\nCompilation complete successfuly.")
                    print("See compiled files in %s" %normalpath)
                except Exception as e:
                    print("Error:", e)
            else:
                print('Error: invalid folder/directry. Try:\n\n',
                      ' Use diretories/folders between double quotes (\"\"). \n',
                      ' Example for (Windows/Linux/Unix(Mac OS)):\n\n',
                      '     # python SPCompiler.py \"c:\\:users\edson lourenco\"'
                      '\n      OR\n',
                      '     # python SPCompiler.py \"/home/edson lourenco\"',
                      '\n      OR\n',
                      '     # python SPCompiler.py \"/users/edson lourenco\"')
        else:
                print("No directory/folder... Try again. ")


def main():
    """Main Function that run."""
    from sys import argv
    dadoEntrada = str(argv[1:])
    dadoEntrada = dadoEntrada.replace("[", "")
    dadoEntrada = dadoEntrada.replace("'", "")
    dadoEntrada = dadoEntrada.replace("]", "")
    objCompiler = Compiler()
    objCompiler.ToCompileAllFiles(dadoEntrada)
if __name__ == '__main__':
    main()
