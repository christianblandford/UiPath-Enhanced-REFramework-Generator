# A uipath-scaffold generator for UiPath Enhanced REFramework
from uipath_scaffold_generator import Generator, Functions
import os, uipath, console_functions as console

#Do the file manipulation for scaffolded files
def edit_scaffolded_files(files_created, should_pass_config=False):
	for file in files_created:
		sequence = uipath.Sequence(file.path)

		#Rename the class
		sequence.set_class_name(Functions.make_project_name(file.name))

		#find the first node
		first_node = sequence.get_first_block()
		#set the description
		sequence.set_annotation(first_node, file.description)
		#Set the block name
		sequence.set_node_name(first_node, Functions.make_project_name(file.name))

		#Set the workblock name
		sequence.get_node_by_display_name("Assign workblock its name").find("InArgument").string = file.name
		sequence.get_node_by_display_name("Create workblock path").find("InArgument").string = file.location

		#Save the file
		sequence.save()

		# If the user specified that they want the config file in all scaffolded sequences
		if should_pass_config:
			#Create a new argument called in_Config with datatype "scg:Dictionary(x:String, x:Object)"
			sequence.add_argument("in_Config", "in", "scg:Dictionary(x:String, x:Object)")
			sequence.add_argument("out_Config", "out", "scg:Dictionary(x:String, x:Object)")