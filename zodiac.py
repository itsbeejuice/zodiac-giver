month=input("What was the exact month of your birth?")
date=input("What day were you born? (please put it in two digit format) ")

if month.lower=="january":
    if date in ["01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20"]:
        print("Capricorn, the tenth sign and mountain goat of the zodiac, is all about hard work. Those born under this sign are more than happy to put in a full day at the office, realizing that it will likely take a lot of those days to get to the top. That’s no problem, since Capricorns are both ambitious and determined: they will get there. Life is one big project for these folks, and they adapt to this by adopting a businesslike approach to most everything they do.")
        capfurther=input("Would you like to know further? Y/N ")
        if capfurther.lower == "y":
            import webbrowser
            webbrowser.open('https://www.astrology.com/zodiac-signs/capricorn')
        elif capfurther.lower == "n":
            print("Fair enough, have a good day^^")
        else:
            print("good day! Peace be with you!")
    elif date in ["21","22","23", "24", "25","26","27","28","29","30","31"]:
        print("Aquarius is the eleventh sign of the zodiac, and Aquarians are the perfect representatives for the Age of Aquarius. Those born under this horoscope sign have the social conscience needed to carry us into the new millennium. Those of the Aquarius zodiac sign are humanitarian, philanthropic, and keenly interested in making the world a better place. Along those lines, they’d like to make the world work better, which is why they focus much of their energy on our social institutions and how they work (or don’t work)")
        aqufurther1=input("Would you like to know further? Y/N ")
        if aqufurther1.lower=="y":
            import webbrowser
            webbrowser.open('https://www.astrology.com/zodiac-signs/aquarius')
        elif aqufurther.lower == "n":
            print("Fair enough, have a good day^^")
        else:
            print("good day! Peace be with you!")

if month.lower=="february":
    if date in ["01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18"]:
        print("Aquarius is the eleventh sign of the zodiac, and Aquarians are the perfect representatives for the Age of Aquarius. Those born under this horoscope sign have the social conscience needed to carry us into the new millennium. Those of the Aquarius zodiac sign are humanitarian, philanthropic, and keenly interested in making the world a better place. Along those lines, they’d like to make the world work better, which is why they focus much of their energy on our social institutions and how they work (or don’t work)")
        aqufurther2=input("Would you like to know further? Y/N ")
        if aqufurther2.lower=="n": #does not match any other indentation level?
            print("Fair enough, have a good day^^")
        elif aqufurther2.lower=="y":
            import webbrowse
            webbrowser.open('https://www.astrology.com/zodiac-signs/aquarrius')
        else:
            print("good day! Peace be with you!")
    elif date in ["19","20","21","22","23","24","25","26","27","28","29"]:
        print("Pisces is the twelfth sign of the zodiac, and it is also the final sign in the zodiacal cycle. Hence, this sign brings together many of the characteristics of the eleven signs that have come before it. Pisces, however, are happiest keeping many of these qualities under wraps. These folks are selfless, spiritual, and very focused on their inner journey.")
        pisfurther1=input("Would you like to know further? Y/N ")
        if pisfurther1.lower=="y":
            import webbrowser
            webbrowser.open('https://www.astrology.com/zodiac-signs/pisces')
        elif capfurther.lower == "n":
            print("Fair enough, have a good day^^")
        else:
            print("good day! Peace be with you!")

if month.lower=="march":
    if date in ["01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20"]:
        print("Pisces is the twelfth sign of the zodiac, and it is also the final sign in the zodiacal cycle. Hence, this sign brings together many of the characteristics of the eleven signs that have come before it. Pisces, however, are happiest keeping many of these qualities under wraps. These folks are selfless, spiritual, and very focused on their inner journey.")
        pisfurther2=input("Would you like to know further? Y/N ")
        if pisfurther2.lower=="y":
            import webbrowser
            webbrowser.open('https://www.astrology.com/zodiac-signs/pisces')
        elif pisfurther.lower == "n":
            print("Fair enough, have a good day^^")
        else:
            print("good day! Peace be with you!")
    elif date in ["21","22","23","24","25","26","27","28","29","30","31"]:
                   print("Aries is the first sign of the zodiac, and that’s pretty much how those born under this sign see themselves: first. Aries are the leaders of the pack, first in line to get things going. Whether or not everything gets done is another question altogether, for an Aries prefers to initiate rather than to complete. Do you have a project needing a kick-start? Call an Aries, by all means. The leadership displayed by Aries is most impressive, so don’t be surprised if they can rally the troops against seemingly insurmountable odds—they have that kind of personal magnetism.")
                   arifurther1=input("Would you like to know further? Y/N ")
    if arifurther1.lower=="y":
        import webbrowser
        webbrowser.open('https://www.astrology.com/zodiac-signs/aries')
    elif arifurther1.lower == "n":
        print("Fair enough, have a good day^^")
    else:
        print("good day! Peace be with you!")

if month.lower=="april":
     if date in ["01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20"]:
        print("Aries is the first sign of the zodiac, and that’s pretty much how those born under this sign see themselves: first. Aries are the leaders of the pack, first in line to get things going. Whether or not everything gets done is another question altogether, for an Aries prefers to initiate rather than to complete. Do you have a project needing a kick-start? Call an Aries, by all means. The leadership displayed by Aries is most impressive, so don’t be surprised if they can rally the troops against seemingly insurmountable odds—they have that kind of personal magnetism.")
        arifurther2=input("Would you like to know further? Y/N ")
        if arifurther2.lower=="y":
            import webbrowser
            webbrowser.open('https://www.astrology.com/zodiac-signs/aries')
        elif arifurther2.lower == "n":
            print("Fair enough, have a good day^^")
        else:
            print("good day! Peace be with you!")
    elif date in ["21","22","23","24","25","26","27","28","29","30"]:
        print("Taurus, the second sign of the zodiac and the ruler of the second house, is all about reward. Unlike the Aries love of the game, the typical Taurus personality loves the rewards of the game. Think physical pleasures and material goods, for those born under this sign revel in delicious excess. This zodiac sign is also tactile, enjoying a tender, even sensual, touch.")
        tarfurther1=input("Would you like to know further? Y/N ")
        if tarfurther1.lower=="y":
            import webbrowser
            webbrowser.open('https://www.astrology.com/zodiac-signs/taurus')
        elif tarfurther1.lower == "n":
            print("Fair enough, have a good day^^")
        else:
            print("good day! Peace be with you!")

if month.lower=="may":
     if date in ["01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20"]:
        print("Taurus, the second sign of the zodiac and the ruler of the second house, is all about reward. Unlike the Aries love of the game, the typical Taurus personality loves the rewards of the game. Think physical pleasures and material goods, for those born under this sign revel in delicious excess. This zodiac sign is also tactile, enjoying a tender, even sensual, touch.")
        tarfurther2=input("Would you like to know further? Y/N ")
        if tarfurther2.lower=="y":
            import webbrowser
            webbrowser.open('https://www.astrology.com/zodiac-signs/aries')
        elif tarfurther2.lower == "n":
            print("Fair enough, have a good day^^")
        else:
            print("good day! Peace be with you!")
    elif date in ["21","22","23","24","25","26","27","28","29","30","31"]:
        print("Gemini is the third sign of the zodiac, and those born under this sign will be quick to tell you all about it. That’s because they love to talk! It’s not just idle chatter with these folks, either. The driving force behind a Gemini zodiac sign’s conversation is their mind. Ruling the third house, the Gemini-born are intellectually inclined, forever probing people and places in search of information.")
        gemfurther1=input("Would you like to know further? Y/N ")
        if gemfurther1.lower=="y":
            import webbrowser
            webbrowser.open('https://www.astrology.com/zodiac-signs/gemini')
        elif gemfurther1.lower=="n":
            print("Fair enough have a good day")
        else:
            print("good day! Peace be with you!")

if month.lower=="june":
    if date in ["01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21"]:
         print("Gemini is the third sign of the zodiac, and those born under this sign will be quick to tell you all about it. That’s because they love to talk! It’s not just idle chatter with these folks, either. The driving force behind a Gemini zodiac sign’s conversation is their mind. Ruling the third house, the Gemini-born are intellectually inclined, forever probing people and places in search of information.")
         gemfurther2=input("Would you like to know further? Y/N ")
         if gemfurther2.lower=="y":
             import webbrowser
             webbrowser.open('https://www.astrology.com/zodiac-signs/gemini')
        elif gemfurther2.lower=="n":
            print("Fair enough have a good day")
        else:
            print("good day! Peace be with you!")
    elif date in ["22","23","24","25","26","27","28","29","30"]:
        print("Cancer, the fourth sign of the zodiac, is all about home. Those born under this horoscope sign are ‘roots’ kinds of people, and take great pleasure in the comforts of home and family.Cancers are maternal, domestic, and love to nurture others.\nMore than likely, their family will be large, too—the more, the merrier! Cancers will certainly be merry if their home life is serene and harmonious.")
        canfurther1=input("Would you like to know further? Y/N ")
        if canfurther1.lower=="y":
            import webbrowser
            webbrowser.open('https://www.astrology.com/zodiac-signs/cancer')
        elif canfurther1.lower == "n":
            print("Fair enough, have a good day^^")
        else:
            print("good day! Peace be with you!")
if month.lower=="july":
    if date in ["01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22"]:
        print("Cancer, the fourth sign of the zodiac, is all about home. Those born under this horoscope sign are ‘roots’ kinds of people, and take great pleasure in the comforts of home and family.Cancers are maternal, domestic, and love to nurture others.\nMore than likely, their family will be large, too—the more, the merrier! Cancers will certainly be merry if their home life is serene and harmonious.")
        canfurther2=input("Would you like to know further? Y/N ")
        if canfurther2.lower=="y":
            import webbrowser
            webbrowser.open('https://www.astrology.com/zodiac-signs/cancer')
        elif canfurther2.lower == "n":
            print("Fair enough, have a good day^^")
        else:
            print("good day! Peace be with you!")
    elif date in ["23","24","25","26","27","28","29","30","31"]:
        print("Leo is the fifth sign of the zodiac. These folks are impossible to miss since they love being center stage. Making an impression is Job #1 for Leos, and when you consider their personal magnetism, you see the job is quite easy. Leos are an ambitious lot, and their strength of purpose allows them to accomplish a great deal. The fact that this horoscope sign is also creative makes their endeavors fun for them and everyone else.")
        leofurther1=input("Would you like to know further? Y/N ")
        if leofurther1.lower=="y":
            import webbrowser
            webbrowser.open('https://www.astrology.com/zodiac-signs/leo')
        elif leofurther1.lower == "n":
            print("Fair enough, have a good day^^")
        else:
            print("good day! Peace be with you!")