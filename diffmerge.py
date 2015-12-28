import sublime, sublime_plugin

sublimePath = r"D:\Sublime Text 3"
difmrgDir = r'C:\Program Files\SourceGear\Common\DiffMerge'
difmrgExe = r'sgdm.exe'

import os
os.chdir(sublimePath)

class DiffmergeCommand(sublime_plugin.WindowCommand):

    def run(self):
        win = self.window

        difmrgPath = os.path.join(difmrgDir, difmrgExe)
        if not os.path.exists(difmrgPath):
            return

        difmrgLhsRhs = []
        for idx in range(min(2, win.num_groups())):
            name = win.active_view_in_group(idx).file_name()
            if name == None:
                break
            difmrgLhsRhs.append('"' + name + '"')

        cmd = ' '.join([difmrgExe] + difmrgLhsRhs)
        
        from subprocess import Popen
        stdout, stderr = Popen(cmd).communicate()
        