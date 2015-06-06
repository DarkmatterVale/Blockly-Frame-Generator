__author__ = 'Vale Tolpegin'

# Importing relevant classes
import sys, os, re

class frame_generator:
    # Initialization method
    def init( self, *args, **kwargs ):
        pass
    
    # Function that delegates frame file generation for every language that was requested
    def generate_frame_files( self, base_directory, languages ):
        for language in languages:
            if language == "propc":
                return self.generate_c_frame( base_directory )
            elif language == "spin":
                return self.generate_spin_frame( self, base_directory )

    # Function that actually generates the frame file for the C language
    def generate_c_frame( self, base_directory ):
        return False
    
    # Function that actually generates the frame file for the Spin language
    def generate_spin_frame( self, base_directory ):
        return False

    # Function that returns the block name and other useful information about the blocks
    def get_blocks( self, path ):
        # Walking the directory to get all of the names of the blocks
        for dirs, files, dir_names in os.walk( path ):
            file = os.open( files, 'r' ).read()

            # TO DO: Parse files to find blocks

        return ""

    # Function that returns the file names of all of the block files
    def get_file_name( self, path ):
        for dirs, files, dir_names in os.walk( path ):
            pass
        
        return ""

    # Opens a directory chooser dialog window and returns the path of the directory the user chose
    def askdirectory(self, **options):
        return apply(self.Chooser, (), options).show()
    
    class Chooser(Dialog):
        
        command = "tk_chooseDirectory"
        
        def _fixresult(self, widget, result):
            if result:
                # keep directory until next time
                self.options["initialdir"] = result
            self.directory = result # compatibility
            return result

class arg_parser:
    # Initialization method for the acommand line arguement parser
    def init( self, *args, **kwargs ):
        pass

if __name__ == '__main__':
    # Get language & other command line arguements
    command_line_arg_parser = arg_parser()
    # TO DO: add way to get arguements

    # Instantiate a frame_generator object
    frame_creator = frame_generator()

    # Get base directory
    base_directory = frame_creator.askdirectory()

    # Call frame_generator object to parse and generate frame file(s)
    generated_truefalse = frame_creator.generate_frame_files( base_directory, languages )

    # If the files were successfully generated
    if generated_truefalse:
        # Let the user know the files were generated successfully
        print ""
        print "[ Info ] Frame files generated"
        print ""
    # Otherwise if the files were not successfully generated
    else:
        # Let the user know the files were not successfully generated
        print ""
        print "[ Error ] Frame files could not be generated due to some unknown error. Please try again"
        print ""