#! /usr/bin/env python
import glob, shutil, os


def getsize (filelname):
    filesize = os.path.getsize(filelname) # Get size of file
    return filesize


source = "/home/sma/Downloads"
destination = "/home/removeable/Musics/Fifty-Years-Music-of-Iran"

downloadlist = os.listdir(source)   # List of download files (music file from singer)

archivelist = os.listdir(destination)   # List of archive files (singer directory)

textlist = list()  # Creat list for musics that copied

for singlemusic in downloadlist:

    if singlemusic.endswith('.mp3') or singlemusic.endswith('.flac') or singlemusic.endswith('.wma'):   # Check files that be music

        singlemusic,singlemusic_extension = singlemusic.split(' - ')   # Romove extension from music file and remain singer name in music file

        for singerdir in archivelist:

            if singerdir == singlemusic:   # Compare music name with  directory name

                singlemusic = singlemusic + " - " + singlemusic_extension    # Add extension to singer name (complete name music)
                src = os.path.join(source,singlemusic)  # Add address file before music file
                dst = os.path.join(destination,singerdir)   # Add address directory before name directory
                existmusic = os.path.join(dst,singlemusic) # Path of single music in archive directory if there are

                if os.path.isfile(existmusic):

                    size_music_file = getsize(src)  # Get size music file in downloaded list
                    size_existing_music_file = getsize(existmusic)  # Get size music file in archive directory

                    print ("musicfile",size_music_file)    # Print size file
                    print ("existing musicfile",size_existing_music_file)   # Print size file

                    if size_music_file < size_existing_music_file: # if size of music file bigger than size music file existing is copy otherwise don't copy
                        continue

                shutil.move(src,dst)    # Copy match music files to directory

                textlist.append(singlemusic)    # Add music file name copied to list

textlist.sort()    # Sort list


copytext = open("List_of_copied_Music_Files", "w+")     # create text file for store list of copied music file

for line in textlist:
    copytext.write(line + '\n')     # add textlist lines to text file

copytext.close()    # close copytext file after copy files

#removetext = open("List_of_removed_copied_Music_Files","w+")    # remove Music files is copied from source directory
#for musicline in textlist:
#    musicline = os.path.join(source,musicline)  # create path of file
#    os.remove(musicline)    # remove music file from source after copied
#    removetext.wirte(musicline + '\n')
#removetext.close() # close removetext file after remove files

