# A uipath-scaffold generator for UiPath Enhanced REFramework
from uipath_scaffold_generator import Generator, Functions
import os, uipath, console_functions as console

def __main__():
	#Set Up A Generator
	enhanced_reframework_generator = Generator("UiPath Enhanced REFramework Generator", 
		"Scaffolds a new Enhanced REFramework Project.", "https://github.com/mihhdu/Enhanced-REFramework/archive/master.zip", os.path.join("Workblock Snippet","wbTemplate.xaml"))

	#Welcome to the generator
	messages = ["Welcome to " + enhanced_reframework_generator.name + "!", "By Christian Blandford", "github: cblandford"]
	console.header(messages, "yellow", "yellow", "=")

	supported_scaffolding_types = ["Project", "All Sequences", "Single Sequence"]
	console.input("Please hit any key to choose the type of scaffolding you would like...", allow_empty=True)
	scaffold_type = supported_scaffolding_types[console.input_list("Scaffolding type: ", supported_scaffolding_types)]
	console.special(scaffold_type)

	if scaffold_type == "Project":
		enhanced_reframework_generator.scaffold_project()

		should_scaffold_files = console.input("Would you like to scaffold out sequences now?", "Y")
		if should_scaffold_files == "Y":
			enhanced_reframework_generator.scaffold_seqeuences()

			should_pass_config = console.input("Would you like to automatically pass the config variable to all sequences?", "Y")
			console.log("Okay, I will pass config to all sequences...")
			if should_pass_config == "Y":
				edit_scaffolded_files(enhanced_reframework_generator.files_created, True)
			else:
				edit_scaffolded_files(enhanced_reframework_generator.files_created, False)

			console.log("Sequence scaffolding complete. Your project is ready!")

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

__main__()
