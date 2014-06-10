FocusFileOnSidebar
==================

Sublime Text has two options regarding its sidebar: `Toggle Side Bar` and `Reveal in Side Bar`, in many (mine :P) workflows people want to browse their files tree right on the opened file's folder, which isn't possible with those two options alone.

This plugin aims to give an easier and simple option that allows the developer to use the new command `Focus File On Sidebar` to open sidebar and move focus right to the opened file's place on project's tree, this way the user can navigate on files tree with keyboard arrows, and use the same command `Focus File On Sidebar` to close sidebar and fold the unfolded folders, preparing it to be used in the same way again (this is needed because if the folder is already opened the focus goes to "opened files" section on the top of sidebar). It's hard to explain how this small changing of focus to the sidebar improved my everyday workflow, I no longer use the `Reveal in Side Bar` command, I'd suggest you to give it a try.

## How to use

By default the plugin adds the `Focus File On Sidebar` command to the command pallete (`control+shift+P`) and adds the shortcut `Ctrl+K, Ctrl+F` (Windows/Linux) or `Cmd+K, Cmd+F` (OSX) to be used faster, obviously you can overwrite this options on your `Packages/User/Default (YourOS).sublime-keymap` file simply by assigning another shortcut to `focus_file_on_sidebar` command.

## How to install

In the same way you can install all the others Sublime plugins, by running a `git clone git@github.com:miguelgraz/FocusFileOnSidebar.git` on your `Packages` folder or, if you use Package Control, just by searching the plugin's name and installing from there.

## Errors? Doubts? How this differs from `Reveal in Side Bar`? Contributing?

You can always send a pull request, send me an email or create an issue with your doubts/feature request/critics =)

I really hope this could be of any use for you!
