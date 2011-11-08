"""
As Above v1.0.0
by Nick Fisher
https://github.com/spadgos/sublime-AsAbove
"""
import sublime_plugin


class AsAboveCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        v = self.view

        for sel in reversed(v.sel()):
            (row, col) = v.rowcol(sel.begin())
            if row == 0:
                continue
            line = v.substr(v.line(v.text_point(row - 1, 0)))
            if (sel.empty()):
                # insert the next character
                if (col < len(line)):
                    v.insert(edit, sel.end(), line[col])
            else:
                # clone the corresponding block from above
                (endRow, endCol) = v.rowcol(sel.end())
                if (endRow != row):
                    continue
                if (endCol >= len(line)):
                    line = line + (" " * (endCol - len(line) + 1))
                v.replace(edit, sel, line[col:endCol])
