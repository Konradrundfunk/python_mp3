from tinytag import TinyTag
tag = TinyTag.get('/home/fingadumbledore/Musik/sound.mp3')
print('This track is by %s.' % tag.artist)
print('It is %f seconds long.' % tag.duration)
print('Album:' , tag.album)         
print( 'Albumartist:' ,tag.albumartist)   
print( 'artist:' ,tag.artist)       
print( 'audio offset:' ,tag.audio_offset)  
print( 'bitrate:' ,tag.bitrate)       
print( 'comment:' ,tag.comment)      
print('composer:' , tag.composer)      
print( 'disc:' ,tag.disc)         
print( 'disc total:' ,tag.disc_total)    
print( 'duration:' ,tag.duration)     
print( 'filesize:' ,tag.filesize , 'Bytes')     
print('genre:' , tag.genre)         
print( 'samplerate:' ,tag.samplerate)    
print('title:' , tag.title)         
print( 'track:' ,tag.track)         
print( 'track total:' ,tag.track_total)  
print( 'year:' ,tag.year)         