# Modern-Wigglegrams
Modernizing wigglegrams with GoPros and python. 
I've been fascinated with wiggle grams. Head over to reddit if you're not sure what they are and want to see some.
https://www.reddit.com/r/wigglegrams/

People usually make these with old Nimslo or Nishika 3D cameras. I think film photography is cool, but for me I didn't want to deal with the hassle of developing film. My modern wigglegram rig uses six GoPro Hero 3+ held together in a custom 3D printed rig. I use a wireless GoPro remote to take all six pictures simultaneously. This configuration would work with any amount of GoPros. Initially I only intended to use four, but I found a great deal for six on eBay.

I plug the GoPros in to my computer and each batch of photos gets dumped into its own folder i.e. "GoPro 1", "GoPro 2"...

wigglegram-sorter.py saves each camera directory as an alphabetized list. It asks for the filename of your desired photo from the first camera, finds the index of that file in the list, then goes to the other lists and gets the name of the other files based on the list. It will also ask for the name of a new folder that it will create and copy the six frames to. The directory paths on this program only work on my computer so you will have to adapt it to fit your use. The code is not complex and you only need very minimal python/programming skills to suit your setup.

good-aligner.py asks for the name of the folder created by wigglegram-sorter.py and uses opencv to align those photos based on the first frame. It creates a folder named "aligned" and puts the finished photos in there. This program is the most applicable to any situtation regardless of your setup. I don't fully understand how opencv image alignment works. I just took the code from Satya Mallick at learnopencv
https://www.learnopencv.com/image-alignment-feature-based-using-opencv-c-python/
All I did was change the alignment function to prevent it from warping the image by restricting the operations to scaling, rotating, and translating. Again, you only need minimal python skills to understand how to edit this for yourself.

I designed the rig in Fusion360 and it gives access to all ports and the wifi button. The only button inaccessible is the capture button, but I use the wireless remote so I don't need it. It was designed to fit the Hero 3+, I'm not sure if it will fit other GoPros.

If you need any clarification for how everything works feel free to email me at ethanjohnsong@gmail.com. If you find a way to make a lot of money with these designs and code, let me know so I can do the same :)

