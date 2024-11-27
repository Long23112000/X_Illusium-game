label shipIntro:

    if hallIntro == False or cabinIntro == False or labIntro == False:
        main "Where should I go?"
        menu:
            "Main hall" if hallIntro == False:
                $ hallIntro = True
                jump hall
            "Main hall" if hallIntro == True:
                main "I already went there."
                jump shipIntro
            "Control cabin" if cabinIntro == False:
                $ cabinIntro = True
                jump cabin
            "Control cabin" if cabinIntro == True:
                main "I already went there."
                jump shipIntro
            "Laboratory" if labIntro == False:
                $labIntro = True
                jump lab
            "Laboratory" if labIntro == True:
                main "I already went there."
                jump shipIntro

    "That seems to be all the important people at least."
    return

label hall:

    hide roomA
    hide cabin
    show hall with fade

    show lt
    lt "Hey Eric, how're you liking the ship so far? Quite comfortable I hope?
        It's certainly faster than any spaceship I've ever been on before."
    "This is the lieutenant, Jack Fare. I've talked with him a few times and he's
    a pretty reliable person. He's been working for the captain for many years now."
    main "Yeah, it's hard to believe that we will make it to Planet X in just a few days.
        I'm a little concerned about the safety."
    lt "We have the best trained pilots in the world here though,
        so I'm fairly confident in their capabilities of handling it."
    lt "Anyway, I gotta go prepare a meeting with the captain. See you later."
    hide lt

    "I see an unfamiliar face."

    show hall with fade

    show eng
    eng "I heard that you are curious about the safety of this spaceship?"
    eng "Why, it is completely safe. It was designed by my team, headed by yours truly.
        It is the perfect transport, combining speed and safety using cutting edge technology."
    eng "As the head engineer, I know the design and functionality of the entire spacecraft.
        It is my pride and joy!"
    eng "Now, if you will excuse me I have important matters to attend to."
    hide eng with moveoutleft

    "I didn't even get to respond."
    "That must've been the head engineer, Dr. Igarashi. I've seen him in the news before,
    but he seems a fair more egotistical than I had originally thought."

    "THUD"
    "Someone shoves me in the back."
    stranger "Oops, my mistake."
    show exp
    exp "Oh, it's you again. Better not get in my way this time."
    hide exp with moveoutright
    main "I was standing still."
    "That was Sue, another scout like me."
    "We had a mission in the past but ran into some trouble because of her
    eagerness triggering a trap, catching both of us."
    "Ever since then, she has been bitter to me. Even though it was her fault."

    "Anyway, let's go somewhere else."

    show hall with fade
    jump shipIntro

label cabin:

    hide roomA
    hide hall
    show cabin with fade

    show cpt
    cpt "I've never seen you before. You are one of the exploration experts, correct?"
    "This is Captain Bychkov. I saw him receiving the mission from the general personally
    yesterday, but I've never actually spoken with him before."
    main "Yes, my name is Eric He. Captain, what do you think of this mission?"
    cpt "This mission will be very difficult. We don't know what those aliens are planning.
        Our planet's future may be decided by this mission."
    cpt "No matter how many sacrifices we make, we must complete this mission.
         As the captain, I will take command and lead us to victory."
    cpt "Now, I must continue preparing for our meeting regarding our plans."
    cpt "I expect to see you there."
    hide cpt with moveoutleft

    "I'd like to hope that there will be no sacrifices."

    stranger "WUWUWUWUWUWUWUWUWUWUWU"
    "I turn towards the source of the sound and look down."
    show monkey
    "...What?"
    hide monkey with moveoutleft
    "Am I hallucinating? Why is there a monkey aboard this ship?"

    "I think I should head back, seemed like that was everyone here."

    show cabin with fade
    jump shipIntro

label lab:

    hide roomA
    hide hall
    hide cabin
    show roomA with fade

    show sci:
        xalign 0.7
    show ast:
        xalign 0.3
    sci "Yes, the dynamic theory of this spacecraft was researched by me.
        In the universe, our human civilization is simply like a small dust particle."
    sci "To have discovered an alien civilization in my lifetime, oh I just can't wait to
        see their technology! Aren't you excited, Cecil?"
    ast "Yes, yes, I get it. You really want to see those aliens up close. It's too bad we are basically at war."

    "That's our researcher, Dr. Newinstein and who I assume is his assistant."

    hide sci with moveoutright
    ast "Hm, who are you?"
    main "Hello, my name is Eric-"
    ast "So you're not a researcher?"
    ast "Then why are you here? We can't risk you breaking any important equipment."
    ast "If you have no business then you should just leave."
    hide ast

    "Stunned by the sudden aggressiveness, I quickly turned away."
    "It seemed like it was just those two here anyway."

    show roomA with fade
    jump shipIntro

################################################################################

label exploration:

    menu:
        "Take the detour to the shelter":
            return
        "Return to the ship as soon as possible" if bad1 == False:
            jump badEnd1
        "Return to the ship as soon as possible" if bad1 == True:
            main "I'm not getting blown up again. I should probably try find the others."
            jump exploration

label badEnd1:

    show mountain with fade
    "I start make the trek back."
    "Everything goes smoothly and I see the ship in sight again."
    "Something doesn't seem right though. I don't see any signs of the captain and the crew."
    play sound "audio/sounds/Plasma gun.mp3"
    pause 3
    play sound "audio/sounds/Plasma gun.mp3"
    pause 2
    play sound "audio/sounds/Plasma gun.mp3"
    "Suddenly, I'm taking fire from unidentified targets."
    main "Oh kurwa!"
    "I quickly dive behind a nearby rock for cover."
    "Unfortunately, there isn't much else for cover and I'm getting suppressed."
    hide mountain with vpunch
    play sound "audio/sounds/Rocket launch.mp3"
    "Eventually an explosive lands and detonates next to me."
    pause 5
    nav "And thus ended Eric's journey."
    nav "He abandoned his teammates, found out and achieved nothing."
    nav "What a sad sad way to end."
    main "Hey piss off, I tried my best ok?"
    nav "Well since you tried \"Oh so hard\", I'm going to give you a reward."
    main "Is it a rebirth in another world with unfair advantages? That would be amazing."
    nav "Very close, but it is the chance to try again from the cave after the sandstorm."
    #show cave with fade
    $ bad1 = True
    main "I don't know why I expected something good."
    jump exploration

################################################################################

label heist:

    menu:
        "Charge right through them.":
            "Charge right through them? Who do I think I am?"
            "I'm not a superhero and I'm definitely not deluded enough to think I am."
            "Even considering what I've been seeing since landing on this crayola planet."
            jump heist
        "Take the air vent" if bad2 == False:
            jump badEnd2
        "Take the air vent" if bad2 == True:
            "I don't know how to stabilize the energy core, maybe I can get some hints somewhere."
            jump heist
        "Try a disguise":
            return

label badEnd2:

    "I unlock a nearby airvent and crawl in."
    hide base2 with fade
    "I successfully drop into the room and find the energy core."
    main "So I just take it?"
    "Seems simple enough."
    play sound "audio/sounds/treasure founds.mp3"
    pause 3
    stop sound
    play sound "audio/sounds/Big alarm.mp3"
    pause 3
    stop sound
    play sound "audio/sounds/Digging process 2.mp3"
    main "What's going on?!"
    "The door swings open behind me."
    alien "Dude, did you remove the energy core?"
    alien "Duuude, that's not cool, it needs to be stabilized before taking it out like that."
    alien "That's like, definitely gonna blow up now."
    alien "Oh nooo, we're like, all totally gonna die because of you dude."
    play sound "audio/sounds/Rocket launch.mp3"
    "I'm hit by a huge explosion which easily wipes out the entire planet."
    nav "Man, you suck dude."
    main "I don't need you telling me that."
    nav "You didn't even find out who the traitor was."
    main "Well, I don't need to anymore. Everyone died. Happy end."
    nav "No, no, no. You can go back and set things straight."
    $ bad2 = True
    show base2 with fade
    "Well what other choice do I have then? I don't know how to stabilize the core."
    "Why can't life be simple."
    jump heist
