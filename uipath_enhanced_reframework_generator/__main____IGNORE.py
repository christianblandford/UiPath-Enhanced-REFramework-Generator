from uipath_enhanced_reframework_generator import *

print("Hello world!")

#Set Up A Generator
enhanced_reframework_generator = Generator("UiPath Enhanced REFramework Generator", 
	"Scaffolds a new Enhanced REFramework Project.", "https://github.com/mihhdu/Enhanced-REFramework/archive/master.zip", os.path.join("Workblock Snippet","wbTemplate.xaml"))

#Welcome to the generator
messages = ["Welcome to " + enhanced_reframework_generator.name + "!", "By Christian Blandford", "github: cblandford"]
terminal.header(messages, "yellow", "yellow", "=")

supported_scaffolding_types = ["Project", "All Sequences", "Single Sequence"]
terminal.input("Please hit any key to choose the type of scaffolding you would like...", allow_empty=True)
scaffold_type = supported_scaffolding_types[terminal.input_list("Scaffolding type: ", supported_scaffolding_types)]
terminal.special(scaffold_type)

if scaffold_type == "Project":
	enhanced_reframework_generator.scaffold_project()

should_scaffold_files = terminal.input("Would you like to scaffold out sequences now?", "Y")
if should_scaffold_files == "Y":
	enhanced_reframework_generator.scaffold_seqeuences()

	should_pass_config = terminal.input("Would you like to sautomatically pass the config variable to all sequences?", "Y")
	terminal.log("Okay, I will pass config to all sequences...")
	if should_pass_config == "Y":
		edit_scaffolded_files(enhanced_reframework_generator.files_created, True)
	else:
		edit_scaffolded_files(enhanced_reframework_generator.files_created, False)

	console.log("Sequence scaffolding complete. Your project is ready!")