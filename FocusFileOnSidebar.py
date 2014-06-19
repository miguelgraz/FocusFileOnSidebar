import sublime, sublime_plugin

def plugin_loaded():
    global close_sidebar_if_opened
    settings_base = sublime.load_settings("Preferences.sublime-settings")
    settings = sublime.load_settings("FocusFileOnSidebar.sublime-settings")
    close_sidebar_if_opened = settings_base.get('close_sidebar_if_opened') if (settings_base.get('close_sidebar_if_opened') is not None) else settings.get('close_sidebar_if_opened')

    settings.add_on_change('reload', lambda:plugin_loaded())
    settings_base.add_on_change('focusfileonsidebar-reload', lambda:plugin_loaded())

# Thanks https://github.com/titoBouzout
# https://github.com/SublimeText/SideBarFolders/blob/fb4b2ba5b8fe5b14453eebe8db05a6c1b918e029/SideBarFolders.py#L59-L75
def is_sidebar_open(self):
    window = self.window
    view = window.active_view()
    if view:
        sel1 = view.sel()[0]
        window.run_command('focus_side_bar')
        window.run_command('move', {"by": "characters", "forward": True})
        sel2 = view.sel()[0]
        if sel1 != sel2:
            window.run_command('move', {"by": "characters", "forward": False})
            return False # print('sidebar is closed')
        else:
            group, index = window.get_view_index(view)
            window.focus_view(view)
            window.focus_group(group)
            return True # print('sidebar is open')
    return True # by default assume it's open if no view is opened

def refresh_folders(self):
    data = get_project_json(self)
    set_project_json(self, {})
    set_project_json(self, data)

def get_project_json(self):
    return self.window.project_data()

def set_project_json(self, data):
    return self.window.set_project_data(data)

class FocusFileOnSidebar(sublime_plugin.WindowCommand):
    def run(self):
        if not is_sidebar_open(self):
            self.window.run_command("reveal_in_side_bar")
            # Without the timeout the command on the pallete doesn't work
            sublime.set_timeout(lambda:self.window.run_command('focus_side_bar'), 100)
        else:
            if close_sidebar_if_opened:
                self.window.run_command("toggle_side_bar")
                sublime.set_timeout(lambda:refresh_folders(self), 100)
            else:
                self.window.run_command("reveal_in_side_bar")
                self.window.run_command('focus_side_bar')
