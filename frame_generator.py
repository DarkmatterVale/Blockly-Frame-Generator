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
        bad_c_blocks = ""
        bad_c_blocks += "set_ramp_step_toward,"
        
        blocks = self.get_blocks( base_directory, 'propc', bad_c_blocks )
        names = self.get_file_names( base_directory, 'propc' )
    
        keepers = ""
        scripts = ""
        
        for block in blocks:
            if block != "":
                keepers += '\n\t\t\t"' + block + '",'
    
        keepers = keepers[ 0 : len(keepers) - 1 ]
        keepers += '\n'
    
        for name in names:
            if name != "":
                scripts += '\n\t\t<script type="text/javascript" src="generators/propc/' + name + '"></script>'
        
        scripts += '\n'
        
        assembled = ""
        assembled += open( os.getcwd() + '/templates/header_template_c.html', 'r' ).read()
        assembled += scripts
        assembled += open( os.getcwd() + '/templates/body_template.html', 'r' ).read()
        assembled += keepers
        assembled += open( os.getcwd() + '/templates/footer_template.html', 'r' ).read()
        
        file = open( base_directory + '/framec.html', 'w' )
        file.write( assembled )
        file.close()

    # Function that actually generates the frame file for the Spin language
    def generate_spin_frame( self, base_directory ):
        bad_spin_blocks = ""
        
        blocks = self.get_blocks( base_directory, 'Spin', bad_spin_blocks )
        names = self.get_file_names( base_directory, 'spin' )
        
        keepers = ""
        scripts = ""
        
        for block in blocks:
            if block != "":
                keepers += '\n\t\t\t"' + block + '",'

        keepers = keepers[ 0 : len(keepers) - 1 ]
        keepers += '\n'

        for name in names:
            scripts += '\n\t' + '<script type="text/javascript" src="generators/spin/' + name + '"></script>'
        
        assembled = ""
        assembled += open( os.getcwd() + '/templates/header_template_spin.html', 'r' ).read()
        assembled += scripts
        assembled += open( os.getcwd() + '/templates/body_template.html', 'r' ).read()
        assembled += keepers
        assembled += open( os.getcwd() + '/templates/footer_template.html', 'r' ).read()
        
        file = open( base_directory + '/frame.html', 'w' )
        file.write( assembled )
        file.close()


    # Function that returns the block name and other useful information about the blocks
    def get_blocks( self, path, language, bad_blocks ):
        blocks = ""
        
        if bad_blocks == "":
            bad_blocks = "----------"
        
        # Walking the directory to get all of the names of the blocks
        for root, dir, file in os.walk( path + "/generators/" + language + "/" ):
            for file_name in file:
                if '.js' in str( file_name ):
                    file_blocks = open( path + "/generators/" + language + "/" + str( file_name ), 'r' ).read()
    
                    file_blocks = file_blocks.split( '\n' )
                    
                    for line in file_blocks:
                        line = line.split( ' ' )
                        
                        name = ""
                        if 'Blockly.Language' in line[0]:
                            name = re.sub( 'Blockly.Language.', '', line[0] )
                        elif 'Blockly.' + language + '.' in line[0]:
                            name = re.sub( 'Blockly.' + language + '.', '', line[0] )
                        
                        block_accept = True
                        if 'propc' in language:
                            for bad_block in bad_blocks.split( ',' ):
                                if bad_block in name:
                                    block_accept = False
                                    
                                    break
                        elif 'spin' in language:
                            for bad_block in bad_blocks.split( ',' ):
                                if bad_block in name:
                                    block_accept = False
                                
                                    break
                        
                        if block_accept:
                            if '.' not in name and name not in blocks:
                                blocks += "," + name
                            elif '.' in name:
                                name = re.sub( '.*', '', name )
                            
                                if name not in blocks:
                                    blocks += "," + name
                                                
                            if '.' not in name and name not in blocks:
                                blocks += "," + name
                            elif '.' in name:
                                name = re.sub( '.*', '', name )
                                                                
                                if name not in blocks:
                                    blocks += "," + name
    
        return blocks.split( ',' )

    # Function that returns the file names of all of the block files
    def get_file_names( self, path, language ):
        names = ""
        
        for root, dir, file in os.walk( path + "/generators/" + language + "/" ):
            for file_name in file:
                if '.js' in str( file_name ):
                    names += "," + str( file_name )

        return names.split( ',' )

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