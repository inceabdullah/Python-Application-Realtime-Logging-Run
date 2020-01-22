import os
import codecs




files = []

lines_file = "py_files_list.txt"

print("reading lines from %s\r\n\r\n" % (lines_file)) 

f = codecs.open(lines_file, "r", encoding="utf8")

pythoned_files = ["python %s  >> logs/%s.log 2>&1 & " % (x.replace("\n","").replace("\r","").replace("\t",""), x.replace("\n","").replace("\r","").replace("\t","").replace("/","_")) for x in f]

print(*pythoned_files, sep="\r\n\r\n")

one_line_code = "".join(pythoned_files)

print("Command:  %s\r\n\r\n" % (one_line_code) )


cmd = '/bin/sh -c "%s"' % (one_line_code)
proc = os.system(cmd)

print("command is run\r\n\r\n")

