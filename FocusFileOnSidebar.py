import sublime
import sublime_plugin


def plugin_loaded():
    global close_sidebar_if_opened
    global settings
    global settings_base

    settings = sublime.load_settings("FocusFileOnSidebar.sublime-settings")
    settings_base = sublime.load_settings("Preferences.sublime-settings")
    plugin_reload()
    settings.add_on_change('reload', plugin_reload)
    settings_base.add_on_change('focusfileonsidebar-reload', plugin_reload)


def plugin_reload():
    global close_sidebar_if_opened
    close_sidebar_if_opened = settings_base.get(
        'close_sidebar_if_opened', settings.get('close_sidebar_if_opened'))


def plugin_unloaded():
    settings.clear_on_change('reload')
    settings_base.clear_on_change('focusfileonsidebar-reload')

# Thanks https://github.com/titoBouzout
# https://github.com/SublimeText/SideBarFolders/blob/fb4b2ba5b8fe5b14453eebe8db05a6c1b918e029/SideBarFolders.py#L59-L75


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
        if not self.window.is_sidebar_visible():
            self.window.set_sidebar_visible(True)
            self.window.run_command("reveal_in_side_bar")
            # Without the timeout the command on the palette doesn't work
            sublime.set_timeout(
                lambda: self.window.run_command('focus_side_bar'), 50)
        else:
            if close_sidebar_if_opened:
                self.window.set_sidebar_visible(False)
                sublime.set_timeout(lambda: refresh_folders(self), 50)
            else:
                self.window.run_command("reveal_in_side_bar")
                self.window.run_command('focus_side_bar')
