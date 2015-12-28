import sublime, sublime_plugin
import sublime_utils

END_BRACES = [")", "}", "]", '"', "'"]
LINE_ENDS = ["\n", "\r"]

class JumpoutCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        view = self.view
        
        region = view.sel()[0]
        if region.a != region.b or region.a == view.size(): # selected some text, or EOF ?
            return

        cursPnt = region.a
        #print("DEBUG:: cursPnt = ", cursPnt)
        ch = view.substr(cursPnt)
        stops = END_BRACES + LINE_ENDS

        while ch not in stops:
            #print("DEBUG:: cursPnt = %d, char = %s"%(cursPnt, ch))
            cursPnt = cursPnt + 1
            ch = view.substr(cursPnt)

        if ch in END_BRACES:
            cursPnt = cursPnt + 1
        
        #print("DEBUG:: cursPnt = %d, char = %s"%(cursPnt, view.substr(cursPnt)))
        sublime_utils.util_set_cursor_point(view, cursPnt)