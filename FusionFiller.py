# Importing sample Fusion Command
# Could import multiple Command definitions here
from .FillerCommand import FillerCommand, FillerUpdateCommand

commands = []
command_definitions = []


# Define parameters for 1st command
cmd = {
    'cmd_name': 'Solid Infill',
    'cmd_description': 'Create infill of a solid part',
    'cmd_id': 'cmdID_FillerCommand',
    'cmd_resources': './resources',
    'workspace': 'FusionSolidEnvironment',
    'toolbar_panel_id': 'Filler',
    'command_promoted': True,
    'class': FillerCommand,
    'app_name': "FusionFiller"
}
command_definitions.append(cmd)


# Define parameters for 1st command
cmd = {
    'cmd_name': 'Update Filler Features',
    'cmd_description': 'Update any out of date Filler Features in the timeline',
    'cmd_id': 'cmdID_FillerUpdateCommand',
    'cmd_resources': './resources',
    'workspace': 'FusionSolidEnvironment',
    'toolbar_panel_id': 'Filler',
    'command_promoted': True,
    'class': FillerUpdateCommand,
    'app_name': "FusionFiller"
}
command_definitions.append(cmd)

# Set to True to display various useful messages when debugging your app
debug = False

# Don't change anything below here:
for cmd_def in command_definitions:
    command = cmd_def['class'](cmd_def, debug)
    commands.append(command)


def run(context):
    for run_command in commands:
        run_command.on_run()


def stop(context):
    for stop_command in commands:
        stop_command.on_stop()
