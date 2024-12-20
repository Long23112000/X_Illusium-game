﻿# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define nav = Character("Narrator")
define main = Character("Eric")
define cpt = Character("Cpt. Bychkov")
define lt = Character("Lt. Fare")
define eng = Character("Dr. Igarashi")
define tech = Character("Adette")
define exp = Character("Sue")
define soldier = Character("David")
define sci = Character("Prof. Newinstein")
define ast = Character("Cecil")
define robot = Character("Britz")
define monkey = Character("Caesar")
define alien = Character("Ambrosian")
define alienA = Character("Ambrosian With Clothes")
define alienB = Character("Ambrosian Without Clothes")
#define alienC = Character("Ambrosian C")
#define alienD = Character("Ambrosian D")
define gbeemz = Character("gbeemz")

define stranger = Character("???")

define hallIntro = False
define cabinIntro = False
define labIntro = False
define bad1 = False
define bad2 = False

# The game starts here.

label start:

    show shipEx
    "It's currently year 3249."
    "Alien life has been discovered and although they have not attacked us yet, their technology far surpasses ours in terms of power."
    "They have introduced their planet as Ambrose."
    "Recent interception of their communications have been decrypted to give us the information of the coordinates of \"Planet X\"."
    "According to the information, this planet holds a large energy source from a past successful civilization."
    "If the ambrosians were to obtain this energy source, they will be a massive threat to Earth."
    "I am Eric, a expert at scouting and my mission, alongside a team of experts, is to secure this energy source from Planet X."
    hide shipEx

    show roomA
    play music "audio/music/xilussim3.mp3"
    show robot
    robot "Greetings, you may call me Britz, I am the robot in charge of your lives on the spaceship.
        If you have any questions, you may contact me, I am everywhere, even in the lavatory."
    hide robot with moveoutleft
    main "For now, I think I should go meet the team and see the people I'm working with."

    call shipIntro from _call_shipIntro

    "Everyone seems to be busy, maybe I'll go back to my room and take a nap."
    hide roomA
    hide hall
    hide cabin

    "My mind drifts off to sleep as I think of what Planet X will hold in store for us."
    "Will it be paradise? Like Elysium? Or a hellhole?"

    stop music
    play sound "audio/sounds/Small alrm.mp3"
    pause 3
    stop sound
    "The alarm?"
    "I rush outside to see the situation."

    show roomA with fade
    show robot
    main "Hey Britz, what's the situation?"
    robot "Our signal receiver caught a strange signal, but we have no way to decipher it. I tried all the methods, but it still doesn't work.
        The captain thinks this signal is suspicious, I hope you can go over to see the situation."
    hide robot
    hide shipIn with fade

    "I rush over to the cabin."

    show cabin with fade
    show cpt
    cpt "It seems that Britz has already told you about the strange signal."
    cpt "I asked Newinstein and he said that these signals did not come from the motion of stars, and certain laws of these signals showed that they came from a civilization!"
    cpt "If the people of Ambrose knows about our plan, they will find ways to prevent us from getting the energy core in advance."
    main "That would lose us the element of surprise. I will go see the doctor and see if we can come up with a few contingency plans."
    hide cpt
    hide cabin

    show roomA with fade
    show sci:
        xalign 0.7
    show ast:
        xalign 0.3
    main "So? Anything new on the signal?"
    sci "I took a look at the frequency of the signal, it is indeed from a certain civilization."
    main "Is it confirmed to be from Ambrose?"
    sci "Please be clear, there are countless civilizations in the universe, and it is too early to say that it comes from Ambrose."
    main "It is most likely to be from Ambrose, as they are the only civilization to communicate with us at this time."
    main "Furthermore, if the signal truly is from Ambrose, this will pose a great risk to our operation."
    ast "You are so ridiculous, I have nothing to say!"
    main "If you have nothing productive to say, then just stay silent."
    sci "Enough, guys, I think we have to check the signal transmitter to make sure that the signal of our spaceship is not caught by other civilizations. It is so dangerous."
    main "Hey hang on, was the signal transmitter ever used since we left Earth?"
    "I go check the transmitter log."
    main "It's been used once right after we left Earth. Why didn't either of you check this first?"
    sci "It has?! You should report this to the captain immediately."
    "How did this get overlooked?"
    hide sci
    hide ast
    hide roomA

    show cabin with fade
    show cpt
    main "Captain, our signal transmitter was used after we took off."
    main "I suspect that strange signal we received may be a reply from the enemy."
    cpt "What? Lieutenant, are you there? I think we are in big trouble."
    show cpt:
        linear 0.5 xalign 0.3
    show lt:
        xalign 1.5
        linear 0.5 xalign 0.7
    lt "Yeah, I heard everything."
    lt "Is there a spy on our ship? We still can't escape the penetration of Ambrose, and for so many years, they seem to be able to penetrate us easily."
    "What? Didn't we decode their communication before to get information on Planet X in the first place?"
    main "Are you saying that Ambrose started spying on Earth a long time ago? Why didn't we know anything about this?"
    cpt "In order to avoid panic from the masses, we have been concealing this secret and trying our best to avoid it."
    "Great, love being told nothing."
    cpt "If the signal is from Ambrose, then there must be a traitor on our ship!"
    hide cpt
    hide lt
    hide cabin with hpunch

    play sound "audio/sounds/Sound.mp3"
    pause 3
    play sound "audio/sounds/Small alrm.mp3"
    pause 3
    stop sound
    stranger "wuwuwwuwuwuwwuwuwuwuwuw~"
    "That stupid monkey needs to shut up."
    cpt "Engineer! What's the status?"
    eng "There's a bit of interference with the auxiliary power affecting the lights, but we should be fine."
    eng "We found a space station that seems to come from the Earth. Do we need to interrupt the voyage and check the situation?"
    cpt "What? How could a human space station be found in such a place? Let's go see what happened."
    eng "If the spaceship decelerates suddenly, it may malfunction!"
    cpt "Don't worry. We can't see others calling for help and ignore them."
    "What happened to the \"We will complete the mission no matter the cost\"?"
    "Maybe the captain is softer than I thought."
    lt "We have detected that some functions of the space station are still working. Maybe there are survivors on it."
    cpt "Scouts! Investigate the space station."
    "I make my way to the exit hatch"
    show exp
    exp "Fasten your belts, I'm not going to bail you out again."
    main "Speak for yourself."
    hide exp
    "We land on the station and find most of it had been destroyed save for a small sector containing a lone soldier."
    show exp
    main "Hello? Who are you?"
    show exp:
        linear 0.5 xalign 0.3
    show soldier:
        xalign 1.5
        linear 0.5 xalign 0.7
    soldier "A rescue squad? My god. My name is David Seidel, a security guard."
    soldier "I have been here alone for fifteen years. They all died fifteen years ago. I have faced loneliness and fear from the depths of the universe alone for fifteen years!"
    soldier "Take me out of here!"
    main "Fifteen years? How did you even survive?"
    exp "We are going to perform important missions, we can contact the Earth Rescue Team to rescue you."
    soldier "Please don't leave me here, please don't, please!"
    main "Hey hold on, there's spare space on our ship, we should ask the captain what he thinks."
    exp "Fine, I hope he is not a loser like you."
    "This woman."
    soldier "Thank you so much, thank you! Lord, you finally answered my prayer."
    hide exp
    hide soldier

    "A few days after David's rescue..."
    "We are preparing to land on Planet X."
    show cabin with fade
    show cpt
    show eng:
        xalign 0.9
    show lt:
        xalign 0.1
    eng "Damn it! I said that sudden deceleration may have a bad effect. Now the engine situation is very unstable!"
    main "What happened?"
    eng "Our spaceship encountered a little trouble, because the sudden slowdown when passing the space station, the problem should have been at that time."
    eng "OH MY GOD! We will all die!"
    main "Oh my god. We will all die."
    main "Alright seriously, what do we do?"
    lt "At this time we must trust the captain, he will surely let us survive!"
    hide cpt
    hide eng
    hide lt
    show cabin with fade
    show monkey:
        xalign 0.7
    show ast:
        xalign 0.2
    monkey "wuwuwuwuuwwwwuwwuwuwwuwuu"
    ast "Ah, look at Caesar, do you know that the sixth sense of animals has always been very accurate, Caesar is so manic, I think we are inevitable!"
    "I think Cecil has had one too many."
    hide monkey
    hide ast
    show cabin with fade
    show cpt
    show eng:
        xalign 0.9
    show lt:
        xalign 0.1
    eng "The engine is malfunctioning! We have no way to slow down when we land! We will hit Planet X like a comet."
    lt "Captain, it's not the ground! It's liquid methane! If we adjust our direction and land on liquid methane, we may still survive!"
    cpt "Maybe this is our only chance to survive!"
    cpt "We can't hit the liquid methane head-on, so our spacecraft cannot withstand the impact."
    cpt "We can only adjust the direction and slow the spacecraft through side friction. We need a long enough buffer distance!"
    lt "Captain, liquid methane hardly flows. I judged by the traces of fluid passing on the rocks over there. It seems that there is liquid methane in the middle of the mountains."
    lt "It seems to be a straight line, but I am not sure whether the buffer distance can be reached!"
    cpt "It seems that I can only spare it! Guys, let's take a gamble!"
    hide cpt
    hide eng
    hide lt
    hide cabin with hpunch
    play sound "audio/sounds/Big alarm.mp3"
    pause 3
    play sound "audio/sounds/Rocket launch.mp3"
    pause 5

################################################################################

label landing:

    "Did we die?"
    "Is this hell? It's not so bad, a bit of pain here and there and a mild headache."
    show shipBroken with fade
    "Oh god."
    "What the hell is that?"
    show cpt with moveinright
    cpt "Hey you, you're finally awake!"
    cpt "Haha, we actually survived! Unfortunately, our ship has taken heavy damage!"
    main "THAT'S our ship?"
    "Maybe this really is hell."
    main "Excellent, stranded on a planet with no means to escape."
    main "By the way, captain, why is there no colour on this planet?"
    cpt "No colour? Did you go colourblind from the crash?"
    cpt "Anyway, you're the last to wake up. Let's go find Britz and we can brief you on your mission."
    "Do people get monochromatic blindness from a crash? Maybe I got hit in the head harder than I thought."
    hide cpt
    hide shipBroken with fade
    show shipBroken with fade
    show cpt:
        xalign 0.3
    show robot:
        xalign 0.7
    robot "Earlier, we discussed that because the atmosphere here is too dense, we could not precisely scan a map from space."
    robot "However, I captured some environmental information and using the information we had, we produced a rough map."
    cpt "That’s great, at least better than getting lost and dying outside without a clue."
    "Well, at least we have a map of the place. That should help with the exploration quite a bit."
    main "Alright, let's take a look."
    #play music "joke"
    play sound "audio/sounds/Map or radar sound.mp3"
    show map
    play music "audio/music/joke.mp3"
    pause 3
    stop sound
    main "...What is this?"
    robot "Impressed by the map, I see. This map was drawn by Caesar and I can confirm that it is quite accurate to our data."
    "I think there's something wrong with Britz's censors, but the map being drawn by a monkey makes sense according to the quality."
    "Also it's a PAPER MAP, why is it beeping as if it's electronic?"
    "I decide not to question that."
    main "Is there a better map?"
    robot "Is that humour I detect? This is the best map we have available at the moment."
    main "No seriously, this is actually usele-"
    cpt "Wait! Look at these mountains carefully. These mountains surround the main peak in the middle, as if they spread out in a circle."
    cpt "The number of mountains is the same as the number of stars in this galaxy!"
    robot "The main peak represents the stars, and planet X is the eighth planet, so the energy core is in the mountains on the eighth circle!"
    cpt "The energy core must be here! Let's go and have a look!"
    "What are they even talking about? Mountains? Peaks? Circles? Are we even looking at the same map?"
    "Is he going to say \"Illuminati confirmed\" next?"
    hide map
    main "Do I really have to go search using this totally well made map?"
    cpt "Oh quit with the jokes, you are to scout that blue area in the north and search for the energy core."
    cpt "Take Sue and Lt. Fare with you."
    cpt "Oh I almost forgot, take the radio with you so we can all communicate."
    stop music
    hide cpt
    hide robot
    hide shipBroken with fade
    show exp:
        xalign 0.3
    show lt:
        xalign 0.7
    show mountain with fade
    exp "My god, what kind of civilization left this thing! Compared with them, we are simply the Stone Age, but we may not know how to use fire!"
    lt "They left nothing, but it seems they left everything! This civilization seems to have jumped to a higher dimension, as if it has been separated from the material."
    sci "Everything they couldn't take turned into energy. This civilization condensed everything that was left into the core of energy!"
    sci "This energy core is sufficient to support the energy demand within my cognition!"
    sci "The energy core emits energy all the time, which seems to indicate that it can instantly destroy the entire galaxy!"
    main "All this energy is hidden in a football size of a rock?"
    sci "Stone? You really don’t know that the sky is high and the earth is thick!"
    "I'll just see myself out."
    main "The wind is picking up, we should hurry in case it gets too strong."
    hide mountain with fade
    show cave with fade
    play music "audio/music/Storm in another planet.mp3"
    main "Is this the energy core?"
    "Was the captain seriously right?"
    "Maybe I'm just that stupid that I don't understand his logic."
    lt "Don't touch it! It’s dangerous, we need professional equipment."
    lt "This black box can shield all energy. It should contain it."
    play sound "audio/sounds/treasure founds.mp3"
    pause 3
    stop sound
    exp "Excellent, we should contact the captain and return to the ship."
    main "Yeah there's a slight issue with that."
    main "There's a massive storm outside at the moment and I'd recommend staying here to weather it out."
    lt "Ah, the storm must be interfering with the radio signal."
    exp "There is no guarantee that the storm will stop soon. We may have to spend days here with no support."
    exp "Returning immediately would be the best option."
    main "But the risk is too-"
    lt "I agree with Sue, we didn't bring much supplies so getting stranded here would not be ideal."
    hide cave with fade
    "With that, we head outside and rush back."
    "However, not even 2 minutes in and we are swept by a sandstorm."
    "Thankfully, I managed to find another cave and hid there for about an hour so not much harm was done."
    hide exp
    hide lt
    show cave with fade
    "Except the fact that I was separated from the other two."
    main "Just splendid. Should've taken my advice, we would've been fine."
    main "Now I'm alone and those two are probably dead."
    main "AND Jack had the radio so I can't even communicate."
    "The day just keeps getting worse."
    "Not to mention the terrible scenery."
    "How has no one questioned this? My head hurts just looking at it."
    "Getting back to the task at hand, Jack also had the energy core so finding him would be first priority to the mission."
    show map
    play sound "audio/sounds/Map or radar sound.mp3"
    pause 3
    stop sound
    "Ugh."
    "Just looking at this gives me a headache."
    "And it's still somehow electronic."
    "Anyway, if I assume the energy core we found was at the blue crap at the top and the base is the green dot with puke in the middle, then I'd say the cave I'm in is somewhere in the grey dots or purple slab."
    "I retraced steps to get to this cave so Lt. Fare and Sue should be further ahead."
    "Either way, if I'm to return to camp or search for them, I need to head in the same direction."
    "The question is, should I take a detour west in case they got lost?"
    "Judging from how bad the storm got, I would assume that green block is some sort of shelter or structure."
    "They may have taken shelter there or tried to power through the storm."
    hide map
    stop music
    "The storm seems to have died down so I should make the choice now."
    hide cave with fade

    call exploration from _call_exploration

    show mountain with fade
    "I start heading back to the ship, but taking a loop around the west to survey the area."
    "As I expected, I found ruins of what used to be a building."
    "However, as I approach, I see signs of a battle."
    main "This is... blood?"
    "Fresh bullet shells, scorch marks and explosions, with splats of red and orange blood, as well as dead Ambrosians littered around."
    hide mountain with fade
    "I rush towards the structure and cautiously investigate."
    stranger "Eric? Is that you?"
    "I look down and see Lt. Fare."
    show lt with fade
    main "Lt. Fare! You're heavily wounded, first aid isn't going to cut it, we need to get some help. Where's your radio?"
    lt "Give it up Eric, support isn't coming."
    main "What do you mean?"
    lt "Listen closely, there was a traitor on our ship. They signalled our crash location and bugged our radio."
    lt "As soon as we got the energy source, the Ambrosians used the sandstorm to catch us off and swarm us."
    lt "I made a last stand here and managed to wipe out all of them, but they got me in the end."
    lt "They captured Sue and probably the crew as well. I'm almost certain their base is east."
    lt "I found a strange vehicle here that seems to still work. Might be useful to you."
    main "Who's the traitor?"
    lt "I don't know, but I know it isn't you or Sue and probably not the captain or that guard named David."
    lt "Listen Eric, I think you're a great decision maker. No matter what, trust that your actions are right."
    lt "And if everyone manages to survive, tell the captain that I'm sorry I couldn't make it back."
    main "..."
    hide lt with fade
    "Jack was gone."
    "From what he said, I'm probably the only one left that can do anything."
    "The traitor isn't Sue, the captain or David."
    "I doubt Dr. Igarashi is the traitor as he wouldn't want his ship destroyed."
    "Unless Britz got hacked, he should be on our side."
    "That leaves Prof. Newinstein and his assistant, Cecil."
    "Oh and that monkey Caesar."
    "Yep. The traitor is definitely the monkey."
    "Anyway, in order to complete the mission, I'll need to re-secure the energy core and rescue Dr. Igarashi to fix the ship to return to Earth."
    "Which means I'll need to infiltrate the Ambrosian base."
    "Alone."
    show mountain with fade
    "Well, for starters I should check the ship for supplies before heading out. I can give the vehicle I got a test run while I'm at it."
    hide mountain with fade
    play sound "audio/sounds/Digging process 2.mp3"
    pause 3
    stop sound
    show shipBroken with fade
    "No signs of Ambrosians or the crew. Looks like Jack was right on the money about them getting captured."
    "The vehicle seems to have some sort of hover technology, though I'm not an engineer so I have no idea how it works."
    "Now that I have supplies, I should get a move on."
    stranger "Are the from the exploration squad?"
    show eng with fade
    main "Dr. Igarashi?"
    "Igarashi slips out from a rock formation and greets me."
    eng "You are that explorer, yes?"
    main "Yeah, we got attacked and I'm the only one left. What happened here?"
    eng "The Ambrosians attacked us, the captain and the rest of the crew were captured. I managed to hide in the chaos."
    main "Damn, I thought that might've happened."
    main "Listen, I know their base is most likely to the east, so I'll try and re-secure the energy core rescue them out."
    eng "I see. Perhaps take this explosive charge with you, it may come in handy when breaching the enemy base."
    eng "It is extremely powerful, so it should destroy anything in your way. Make sure to use it wisely."
    eng "Meanwhile, I will continue on the ship's repairs, it is almost done, so I pray for your success."
    hide eng with moveoutright
    "That being said, how did the Igarashi manage to hide? Could it be possible the Ambrosians didn't capture him on purpose?"
    "Could Igarashi be the traitor?"
    "What could his motive be though? A promise to be able to research Ambrosian technology?"
    "No, he seems like a man too prideful for that."
    "Either way, whether he's the traitor or not, we can't leave this planet without him repairing the ship."
    "So I don't think I have any other choice but to trust him for now."
    show map
    play sound "audio/sounds/Map or radar sound.mp3"
    pause 3
    stop sound
    "This map and its sound are going to haunt my dreams."
    "If the Ambrosian base is to the east, then it's probably near that lake in the white patch, similar to our ship landing site."
    hide map
    "If I'm going to find it then the fastest way will be to just head straight there then look around."
    "Luckily, that hover vehicle I have can be used to get there quickly."
    hide shipBroken with fade
    play sound "audio/sounds/Digging process 2.mp3"
    pause 5
    stop sound

################################################################################

label infiltration:

    main "Looks like I was right on the money."
    show base1 with fade
    "No need for any conspiracy theory like angle of a specific moon to see a arbitrary number of structures to find their base."
    "Also it looks just as crap as everything else here. Though definitely better than our ship. Not that that's much of a compliment."
    "If I had to guess where my crew is being held captive, it'd probably be either down near the bottom, or on the top left tower."
    "I think the best route would be to investigate the top tower first, as it's easier to get to."
    hide base1 with fade
    "I quietly loop around and drop down using my grapple."
    "The security is actually terrible."
    "The guards seem to be bunched together inefficiently and most of the windows aren't even closed. I peep into each of the rooms as I scale down."
    "Eventually, I find my crew."
    "They're locked inside rooms next to each other, with only one guard."
    "They probably have the key, so if I can take him out, it'll make the first step of getting out alot easier."
    "I drop into a unlocked room."
    play music "audio/music/Can be a back ground music ( mystery and dangerous).mp3"
    show base2 with fade
    "Alright, I'm in."
    "Actually looks very similar to a human living environment."
    "There's a nice toilet in the room."
    show alienClothed
    "I peep around the corner and see the lone guard."
    "Probably best not to open fire and attract attention, so I make a sound on purpose to attract them."
    hide alienClothed with moveoutbottom
    "They lumber closer and then I rush around the corner, take him down and drown him in the toilet."
    "After some gurgling, they stop resisting."
    alien "Yo, who's there?"
    "Yo?"
    show alienClothed with moveinleft
    "Another guard walks over to see the scene."
    "I quickly hide behind the door."
    alien "Eh? What happened here?!"
    hide alienClothed with moveoutbottom
    "I take him down from behind and drown him in the same toilet."
    "After resistance has ceased, I take the keys and quietly open one of the doors."
    show exp
    exp "Eric?! How did you get here?"
    main "Can it, will you? Can't you see I'm trying to break everyone out here?"
    exp "The others should be in the rooms next to mine."
    hide exp
    hide base2 with fade
    show base2 with fade
    "I unlock everyone's rooms."
    show cpt:
        xalign 0.1
    show exp:
        xalign 0.4
    show robot:
        xalign 0.7
    show soldier:
        xalign 1.0
    cpt "Well done Eric! Now we have a chance to survive. Any ideas on how to escape?"
    main "First of all, wheres Prof. Newinstein and his assistant?"
    robot "When we were captured, those two were separated from us."
    soldier "Could they be traitors?"
    "I never considered that there could be more than one."
    "Although if they're the traitors, that means Igarashi shouldn't be."
    "Which would be great since we need him to fix the ship anyway."
    "I thought that the overlooked use of the transmitter was suspicious. Perhaps I should've been more alert back then."
    cpt "It is possible, but we need have two objectives now."
    cpt "Re-take the energy core and get the hell out of here."
    cpt "If we can save Prof. Newinstein and his assistant we should, but those two objectives take a higher priority now."
    main "Got it, I'll try and find the energy core, perhaps someone should try and secure an escape route?"
    exp "I saw a good escape route from my room. I'll guide everyone there then evacuate for now."
    cpt "Sounds like a good plan, let's move."
    hide cpt with moveoutleft
    hide exp with moveoutleft
    hide robot with moveoutleft
    hide soldier with moveoutleft
    "Is it even surprising anymore that I'm left alone to the most dangerous task?"
    "I better get a raise after this. Or a lifetime supply of vacations."
    "Anyway, if I had to guess where the energy core is, it'd be at the centre of this building."
    "As mentioned earlier, the security of this place is abyssmal."
    "Perhaps they didn't expect a survivor, let alone a person adept at infiltration."
    "I make my way down, avoiding Ambrosians along the way."
    "I pass by a few rooms to see an important looking room guarded by two Ambrosians and a... dog?."
    "I have a few options here."

    call heist from _call_heist

    "This is such a stupid idea, if it works these Ambrosians are dumb as bricks."
    "I just casually walk up to the guards."
    play music "audio/music/joke.mp3"
    show alienClothed
    show alienNaked:
        xalign 0.0
    show gbeemz:
        xalign 1.0
    alienA "Dude, who're you?"
    "Not what I expected."
    main "Uh, dude, it's me, I'm just in a human outfit."
    alienB "Ohhh, that totally makes sense dude."
    alienA "So yeah dude, we were just talking about this human thing called \"music\""
    alienB "Yeah dude, like, that thing called hip hop. Totally tubular. Dude, you know anything about it?"
    main "Yeah totally. Like there's one about mom's spaghetti but it wouldn't come out."
    main "Or this cool dude, who's a spiritual lyrical miracle individual."
    alienA "Duuude, that's like, radical. You should tell us more about it."
    main "Yeah, but I like, kinda got lost dude. I heard some real humans got caught, like, where could I see them?"
    alienA "Dude, we saw them pass by a while ago, they just went down that hall to the left actually."
    alienB "Yeah, you must've, like, just missed them dude."
    main "Oh I see, by the way, could you tell me what's through this door dude?"
    alienA "Yeah sure dude, it's where this thing the higher ups call the energy core is."
    alienB "I heard it's unstable right now, you need to like, unclip the clamps in the right order to restabilize it."
    alienA "If you don't, then it goes kaboom dude! Enough force to wipe out the planet and more, crazy right?"
    alienA "Yeah, if you ever wanna remove it, make sure you remove them from the thinnest to thickest latches dude."
    main "Yeah totally, anyway I gotta go dude."
    alienB "Catch you later, dude. Share some more of that miracle guy next time."
    gbeemz "gbeemzjugzer!"
    stop music
    hide alienClothed
    hide alienNaked
    hide gbeemz
    show base2 with fade
    "Nice, I managed to get some important information on the professor and how not to blow up the planet by accident."
    "I like how the dog wasn't even good enough to sniff me out."
    "I should secure the core, then take the professor and escape."
    "I unlock the air vent and crawl in."
    hide base2 with fade
    "I enter the room and unlock and re-take the energy core."
    play sound "audio/sounds/treasure founds.mp3"
    pause 4
    stop sound
    "I then exit the way I came from and head towards the room."
    show base2 with fade
    stop music
    "I bump into a familiar face."
    show ast
    ast "Eric?!"
    main "You're Cecil, right?"
    ast "Yes, come with me."
    main "Where's Prof. Newinstein?"
    ast "He died, the Ambrosians killed him."
    main "..."
    ast "You will be caught if you stand there, hurry and follow me."
    main "No, everyone else has escaped except us. We should leave, I have an escape route ready."
    hide ast
    "I turn around to move but I hear a click behind me and instinctively move to a corner."
    play music "audio/music/game_audio_music_xillusim_action.mp3"
    play sound "audio/sounds/Plasma gun.mp3"
    "A laser beam zaps right past where I was standing."
    show ast
    ast "Oh, Eric, why did you have to ruin everything?"
    main "I knew it, the traitor was you wasn't it?!"
    main "What really happened to Prof. Newinstein?"
    ast "Why, I killed him myself to prove my loyalty to the Ambrosians."
    main "Are you mad? Why turn against your own kind?"
    show ast:
        linear 0.5 xalign 0.7
    show alienClothed:
        xalign 0.0
    alien "Yo dude, what's up?"
    ast "Perfect timing. I caught a rat, he probably stole the energy core we need and is planning on running away with it."
    alien "Hey dude, that's not cool. We like, need that energy core for stuff back at home dude."
    "The situation just gets worse."
    ast "About your question earlier, I just want to punish you, since I was a child, I vowed to teach you stupid humans a lesson, and today finally has a chance!"
    ast "Human greed and evil have hurt me since I was a child, but I did not collapse, but secretly vowed to retaliate against you hahahaha"
    "The hell is wrong with this guy?"
    alien "Uh, dude you okay?"
    ast "Yes, just seize him."
    play sound "audio/sounds/Rocket launch.mp3"
    hide ast
    hide alien
    hide base2 with vpunch
    "What the...?"
    exp "Better hold tight or die, Eric!"
    main "Sue?"
    "We drop a few floors but Sue's mechanical body absorbs the impact for us."
    show exp
    exp "You weren't coming back so I scouted for you from outside."
    exp "Luckily, I saw you getting caught by Cecil. What happened with him?"
    main "He's the traitor. He said Prof. Newinstein was killed by him and that he's exacting revenge on humanity."
    exp "Sounds like a lunatic. Got the core?"
    main "Yeah."
    exp "Then let's bail. Follow me."
    hide exp with moveoutright
    "We rush through a series of tunnels in the lower portion of the base. I have no idea where we are going until we reach the light at the end."
    show base1 with dissolve
    "We are one floor above the main floor, taking the exit that leads to a narrow path near the wall."
    exp "This is where things get dangerous. Just keep running."
    "We make a mad dash for the sewer entrance, halfway through climbing the stairs they discover us."
    play sound "audio/sounds/Plasma gun.mp3"
    pause 2
    play sound "audio/sounds/Plasma gun.mp3"
    pause 1
    play sound "audio/sounds/Plasma gun.mp3"
    hide base1 with fade
    show base3 with fade
    "Thankfully, we manage to make it while narrowly avoiding getting melted."
    main "So now what?"
    exp "This sewer will lead to the surface, let's not waste any more time."
    hide base3 with fade
    "After traversing through the mossy sewers with surprisingly clean water, we reach the surface."
    show mountain with fade
    show soldier:
        xalign 0.7
    soldier "Sue! Eric! You're both okay!"
    "David is on a vehicle similar to a 4x4 that seems to use hover technology similar to the bike I had earlier."
    show exp:
        xalign 0.3
    exp "David, we need to get out of here right now!"
    soldier "Copy!"
    "We get on the ride and leave as fast as we can."
    hide exp
    hide soldier
    hide mountain with fade
    play sound "audio/sounds/Digging process 2.mp3"
    pause 5
    stop sound
    show shipBroken with fade
    show cpt:
        xalign 0.2
    show eng:
        xalign 0.5
    show robot:
        xalign 0.8

    "I see the ship is still the same as ever. I approach the crew discussing the ship."
    cpt "Ah, you've returned, Eric!"
    main "Can we lift off yet? Or is the ship still screwed?"
    eng "There were only minor damages because the shield system I designed is superior."
    eng "The only issue is we have no energy as the crash depleted it all."
    main "Can we use this energy core then?"
    eng "I'm not too sure, as it seems like it may be incompatible with our generator."
    robot "I can read that it is designed to release energy in every direction when activated."
    robot "If we can somehow get the energy into a single point, it will likely be compatible with our ship."
    eng "I see, then if we use this reflective material, we may be able to funnel the energy into one direction."
    cpt "I don't know what you're planning, but whatever it is it's worth a shot. Otherwise, we die for sure."
    "As the Dr. Igarashi and Britz works on applying the source, this time it is my turn to pray for their success."
    eng "Moment of truth! Let's take off!"
    hide cpt
    hide eng
    hide robot
    hide shipBroken with fade
    "We start what could be the final countdown."
    robot "3"
    pause 1
    robot "2"
    pause 1
    robot "1"
    pause 1
    stop music
    play sound "audio/sounds/Rocket launch.mp3"
    pause 3

label Ending:

    play music "audio/music/xilussim_ badend1.mp3"
    show cabin with fade
    show cpt
    cpt "I see, so Cecil was the traitor. I should have done a more detailed background check."
    cpt "I will take all responsibility when we return."
    main "We also lost Lt. Fare."
    cpt "Yes, he was the best person I've ever worked with. Reliable, knowledgeable, an adept fighter and a close friend."
    cpt "It'll be hard to report this to his family later."
    cpt "As for Prof. Newinstein, it'll be a hit to the science department, but they should recover."
    cpt "Anyone else?"
    main "Hmmm..."
    main "Wait, didn't we have a monkey with us? What was his name again? Cedar?"
    cpt "..."
    hide cpt with moveoutleft
    cpt "MONKEY NOOOOO!"
    "Huh."
    "Maybe it was his pet monkey or something."
    show exp with moveinright
    exp "Hey."
    main "Oh, what's up?"
    exp "...Good job."
    main "What?"
    exp "If not for you, we would've been killed and the energy core would've been in the Ambrosian's hands."
    exp "So I'd like to say good job."
    main "Oh, uh thanks."
    "I somehow don't think the Ambrosians are a threat to us now. Not after talking to them for a bit."
    main "But I definitely would've gotten wiped out if you didn't come back for me so all's well that ends well eh?"
    exp "Heh, you're right."
    hide exp
    hide cabin with fade

    nav "Wow that was a trash story."
    main "Care to explain why I was tripping balls on the planet?"
    nav "Uhhh we ran out of budget."
    main "Seriously? You suck."
    nav "Hey shut up ok? You try draw on demand without practice."
    "The End"

    return
