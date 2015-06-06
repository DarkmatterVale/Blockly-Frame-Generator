__author__ = 'Vale Tolpegin'

# Importing relevant classes
import sys, os, re
import argparse
from tkCommonDialog import Dialog

class frame_generator:
    # Initialization method
    def init( self, *args, **kwargs ):
        pass
    
    # Function that delegates frame file generation for every language that was requested
    def generate_frame_files( self, base_directory, language ):
        if language == "propc":
            self.generate_c_frame( base_directory )
        elif language == "spin":
            self.generate_spin_frame( base_directory )

        return True

    # Function that actually generates the frame file for the C language
    def generate_c_frame( self, base_directory ):
        self.get_blocks( base_directory, 'propc' )

    # Function that actually generates the frame file for the Spin language
    def generate_spin_frame( self, base_directory ):
        return False

    # Function that returns the block name and other useful information about the blocks
    def get_blocks( self, path, language ):
        # Walking the directory to get all of the names of the blocks
        for root, dir, file in os.walk( path + "/generators/" + language + "/" ):
            for file_name in file:
                if '.js' in str( file_name ):
                    print str( file_name )
    
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

if __name__ == '__main__':
    # Get language & other command line arguements
    parser = argparse.ArgumentParser( description="frame generator for BlocklyProp" )
    parser.add_argument( '-c', help='Generate the propc frame file' )
    parser.add_argument( '-s', help='Generate the spin frame file' )
    args = parser.parse_args()

    # Instantiate a frame_generator object
    frame_creator = frame_generator()

    # Get base directory
    base_directory = frame_creator.askdirectory()
    
    # Setting up variables
    languages = ""
    generated_truefalse = False
    
    # If C or Spin is supposed to be parsed, parse them & generate the frame files
    if 'c' in args:
        generated_truefalse = frame_creator.generate_frame_files( base_directory, 'propc' )
    
    if 's' in args:
        generated_truefalse = frame_creator.generate_frame_files( base_directory, 'spin' )

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