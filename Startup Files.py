# Default imports
import sublime
import sublime_plugin

# Run the command at startup
def plugin_loaded():
	sublime.run_command("open_startup_files")

# Ensure all specified files are opened and assigned a tab
class OpenStartupFilesCommand(sublime_plugin.ApplicationCommand):
	def run(self):
		setfiles = sublime.load_settings("Preferences.sublime-settings").get("open_files_at_startup", [])
		openfiles = [view.file_name() for window in sublime.windows() for view in window.views()]
		[sublime.active_window().open_file(file) for file in setfiles if not file in openfiles]

# Set the list of files to all currently open files
class SetStartupFilesCommand(sublime_plugin.ApplicationCommand):
	def run(self):
		sublime.load_settings("Preferences.sublime-settings").set("open_files_at_startup", \
			[view.file_name() for window in sublime.windows() for view in window.views()])
		sublime.save_settings("Preferences.sublime-settings")
