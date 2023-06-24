import time
import random
# note that this a text math game with a dark theme. There are plans to reformat it to be child friendly.
# insert the createcharacter() here
def createcharacter():
	#This very first part decides the character's name and gender.
	malenames = ["Andrew","Anthony","Angel","Abel","Alexander","Allen","Alan","Aaron","Axel","Adam","Ari","Abraham","Antonio","Augustus","Amir","Abdi","Alfred","Alvin","Andre","Andres","Arthur","Angelo","Albert","Arman","Ace","Alejandro","Armando","Bernard","Bjorn","Bernie","Barney","Bailey","Billy","Barry","Ben","Bruce","Benjamin","Booker","Bob","Barnabus","Baird","Brian","Bryan","Brock","Boggy","Boris","Christopher","Claude","Charles","Cornelius","Charlie","Chris","Carl","Chase","Corey","Connor","Craig","Clifford","Cyrus","Chopper","Chad","Constantine","David","Dominic","Dominick","Domenick","Dan","Daniel","Daven","Darius","Don","Donald","Dick","Darren","Daryl","Dwayne","Dane","Drake","Desmond","Doc","Dennis","Dimitri","Dale","Dante","Edgar","Edward","Edwin","Edmond","Edmund","Ed","Edd","Eric","Eddie","Elijah","Elton","Ernie","Frank","Fred","Fredrick","Frederick","Frederico","Forest","Falco","Fenton","Gary","Garry","Greg","Gabriel","Gregg","Gerard","Gilbert","Glen","Glenn","Hank","Herbert","Hercules","Hani","Hugo","Hector","Horace","Harry","Harold","Igor","John","Jacob","Jon","Jesus","Jakub","Jeremy","Jonathan","Jeffrey","Johanathan","Johnathan","Jaime","Jamie","James","Jerry","Jim","Jimmy","Junior","Jack","Jake","Jeremiah","Josh","Joshua","Jaquan","Kris","Kristopher","Ken","Kenny","Kenneth","Kyle","Konstantine","Kristofer","Kobi","Kobe","Kevin","Keith","Lewis","Luis","Lambert","Linus","Loki","Lonny","Lenny","Luke","Lucas","Lester","Lukas","Lars","Lance","Loren","Marcus","Mark","Markus","Marc","Michael","Leslie","Larry","Lawrence","Mike","Mikhail","Martin","Marty","Melvin","Morgan","Mallow","Matthew,","Matt","Manny","Moe","Max","Morris","Milo","Montel","Maximus","Mordred","Merlin","Nathan","Nathaniel","Nick","Nicholas","Nikolas","Neil","Nik","Noggy","Oggy","Ozzy","Oswald","Oliver","Oz","Orlan","Orion","Omar","Peter","Piotr","Patrick","Pablo","Paco","Packie","Patrizio","Perseus","Pat","Paul","Poe","Paulie","Quin","Quinn","Quenton","Quinten","Quintin","Quade","Richie","Richard","Rich","Ryan","Ron","Ronald","Remy","Randy","Raymond","Rupert","Randolph","Randolf","Regnier","Raz","Rick","Ricky","Ricardo","Raul","Robert","Rob","Roc","Rocco","Sam","Samuel","Sargon","Steve","Steven","Stephen","Stephan","Syed","Sammy","Saul","Sean","Shawn","Sal","Salvatore","Simon","Stuart","Stu","Stewart","Sonny","Thomas","Thom","Tom","Travis","Tim","Timothy","Tyler","Toren","Terry","Tor","Theodore","Thor","Tai","Uther","Ulfric","Ugo","Vincent","Vance","Vinny","Vin","Wen","Waldo","Walter","Wayne","William","Will","Wally","Xin","Xavier","Yuri","Zoro","Zack","Zackary","Zachary","Zach","Zane"]
# There are about 309 male names.
	femalenames = ["Anna","Ana","Annie","Alexandra","Agatha","Althea","Arlene","Ali","Amaya","Amy","Alexa","Alana","Alice","Alissandra","Angel","Amanda","Alexandria","Ami","Anya","Anju","Aria","Anne","Ann","Allison","Allyson","Aniyah","Brittany","Britt","Beth","Bethany","Barbara","Bonnie","Bonny","Becca","Bekah","Bess","Bessany","Christina","Christine","Courtney","Christin","Celestine","Christi","Cristi","Carri","Caroline","Carolina","Carolea","Caylee","Cate","Catelyn","Celia","Cecelia","Casandra","Cassy","Casaundra","Corrin","Carmen","Constantina","Cornelia","Cora","Dalia","Dalila","Delilah","Dani","Danielle","Dorris","Debra","Deborah","Destiny","Dana","Dorothy","Dora","Denise","Dolores","Dori","Diane","Donna","Doreen","Dawn","Deanna","Dina","Deena","Dee","Ella","Elle","Ellie","Elvira","Ester","Erica","Elizabeth","Elisabeth","Elena","Eileen","Emily","Erin","Eve","Evie","Frida","Frita","Flor","Fay","Freya","Fran","Francesca","Fanny","Gayle","Gail","Gwen","Gweneth","Gloria","Gabrielle","Guadalupe","Gabriella","Geanine","Gee","Georgina","Gela","Hailey","Hanna","Hannah","Haley","Harrah","Hela","Hellen","Helena","Hermoine","Holly","Irene","Irena","Ilana","Ilene","Ingrid","Jerri","Jerrine","Jeanine","Jovanna","Joyanna","Joy","Jane","Jayna","Jean","Jeanie","Jen","Jennifer","Jamie","Jackie","Jacquelyn","Jaquelyn","Julie","Julia","Jacqueline","Joanne","Jodie","Jesebelle","Jazmine","Jasmine","Krista","Kristin","Kirstin","Kristina","Kristine","Konstantina","Kaylee","Karen","Kora","Katelyn","Kate","Katie","Korrin","Kassy","Kasandra","Khaleesi","Kairi","Kasaundra","Kelly","Kylie","Kairi","Kari","Kendra","Kendria","Leslie","Loria","Lena","Lora","Laura","Lauren","Laurie","Leyla","Leelah","Lorelei","Luna","Lee","Linda","Lexi","Mika","Mariah","Melody","Melissa","Marie","Mary","Maria","Morticia","Marnie","Mable","Monique","Monica","Miley","Michelle","Michele","Molly","Micelle","Madeline","Mikela","Michaela","Monika","Marjorie","Moria","Maureen","Melony","Melinda","Melissandra","Moreen","Nelly","Nicole","Nikki","Nancy","Ovelia","Ophelia","Olivia","Omnia","Odessa","Patricia","Penelope","Persephone","Paula","Pauline","Paulina","Pat","Polly","Polina","Quintana","Quina","Rachel","Renee","Rebecca","Raven","Raquel","Racquel","Reyna","Roni","Rori","Sally","Sara","Sarah","Sonia","Saria","Selene","Susan","Suzanne","Susie","Selena","Selestine","Simone","Selestina","Sandy","Sharon","Saliyah","Sandra","Saundra","Sasha","Trish","Tricia","Tess","Tish","Trisha","Theresa","Therese","Teresa","Terese","Talia","Taliyah","Thea","Theodora","Tyrene","Tabatha","Terry","Tracy","Tyanna","Tianna","Tiara","Tyara","Tylena","Tracey","Ula","Vinchenza","Valerie","Victoria","Vicky","Vick","Vickie","Wilma","Xena","Xaria","Yuri","Yolanda","Zena","Zalia","Zaria"]
#There are about 309 female names.

	lastnames = ['Akina', 'Alderman', 'Aliaga', 'Almog', 'Amelkin', 'Angeles', 'Ansari', 'Appel', 'Arena', 'Arias', 'Armstrong', 'Arriaga', 'Ashworth', 'Baez', 'Bannister', 'Barclay', 'Beal', 'Benson', 'Bergen', 'Bhuyan', 'Braver', 'Bravo', 'Breakstone', 'Briody', 'Brodowski', 'Brown', 'Buchanan', 'Buckmeier', 'Calderon', 'Callahan', 'Carberry', 'Carny', 'Casler', 'Castle', 'Castler', 'Cerruti', 'Chandler', 'Chang', 'Chi', 'Chilelli', 'Chong', 'Christobek', 'Cleland', 'Cleveland', 'Clott', 'Cohen', 'Collins', 'Colon', 'Cotto', 'Dapelo', 'Dartt', 'Das', 'Dauman', 'Davidson', 'Davila', 'Day', 'Dayan', 'Deluna', 'Demasi', 'Derby', 'Dey', 'Diamond', 'Dieckmann', 'Dipietro', 'Dobre', 'Doherty', 'Dolan', 'Dougherty', 'Douglas', 'Douglass', 'Doyle', 'Duffy', 'Dunbar', 'Durant', 'Eacho', 'Edwards', 'Eliassaint', 'Escobar', 'Exantus', 'Failla', 'Fakury', 'Falzone', 'Fayman', 'Feerst', 'Feinman', 'Figman', 'Fischer', 'Fisher', 'Fishkin', 'Flyer', 'Gachette', 'Galper', 'Gentile', 'Ginensky', 'Goldberg', 'Goldfarb', 'Gookin', 'Grant', 'Green', 'Greene', 'Groaner', 'Gronningsater', 'Gu', 'Hagler', 'Hannay', 'Haper', 'Heaney', 'Heinrich', 'Heyman', 'Himselson', 'Hopkirk', 'Horowitz', 'Huang', 'Hughes', 'Humbert', 'Hutchinson', 'Ierardi', 'Iheanachor', 'Illym', 'Ingelson', 'Isdokwe', 'Jafari', 'Jaffe', 'Jagielski', 'Johnson', 'Jones', 'Kean', 'Kharlamenko', 'Kishnani', 'Klengler', 'Klopfer', 'Kogan', 'Komar', 'Korek', 'Koretz', 'Kujo', 'Kurtz', 'Lane', 'Langsam', 'Laspina', 'Lerner', 'Lesher', 'Levin', 'Liben', 'Lieberman', 'Lietz', 'Liu', 'Lubin', 'Lubow', 'Lyons', 'Malhotra', 'Malone', 'Maloney', 'Manini', 'Mardirossian', 'Mariani', 'Marrero', 'Marrufo', 'Martinez', 'Mazarin', 'McDonnel', 'McGoldrick', 'McHugh', 'McNamara', 'Mease', 'Medici', 'Meehan', 'Meggett', 'Mehta', 'Mennin', 'Meyer', 'Miles', 'Millan', 'Miller', 'Mills', 'Mirabella', 'Moroney', 'Morrell', 'Morril', 'Murray', 'Musso', 'Nedich', 'Neri', 'Nicolay', 'Nolan', 'Novak', 'Novillo', 'Novis', 'Nowak', "O'Toole", 'Obus', 'Ortsman', 'Pang', 'Paolillo', 'Paple', 'Park', 'Parker', 'Pasinkoff', 'Pate', 'Pathmanathan', 'Payne', 'Peltier', 'Pemberton', 'Perbix', 'Perez', 'Perks', 'Perlin', 'Perlstein', 'Pesin', 'Pierce', 'Poole', 'Poppish', 'Quan', 'Rankin', 'Ransdell', 'Rapisarda', 'Rappaport', 'Reade', 'Redding', 'Redmond', 'Rendeiro', 'Rene', 'Rezai', 'Richman', 'Richmond', 'Ringer', 'Rivera', 'Roberts', 'Robitaille', 'Rodrigues', 'Rodriguez', 'Rosenblum', 'Ross', 'Rossman', 'Rottenberg', 'Roussel', 'Rowe', 'Rozovsky', 'Ruffin', 'Ruger', 'Ruglia', 'Rutger', 'Salters', 'Santo', 'Sattar', 'Scarcella', 'Schiavone', 'Schwartz', 'Seabrooks', 'Serette', 'Sessa', 'Shah', 'Shapovalova', 'Shin', 'Silberman', 'Silverman', 'Simchi', 'Sims', 'Slater', 'Smith', 'Sohn', 'Sorett', 'Stanziale', 'Stearn', 'Stearns', 'Stengel', 'Stephenson', 'Stevens', 'Stevenson', 'Stocking', 'Swensen', 'Swenson', 'Tian', 'Tibbets', 'Tirrell', 'Todadze', 'Toder', 'Tuccio', 'Tucker', 'Tyrell', 'Ukomedu', 'Umber', 'Umbert', 'Urena', 'Valentine', 'Vargas', 'Vasques', 'Vasquez', 'Ventura', 'Villaamil', 'Vogelman', 'Volk', 'Voshtina', 'Walker', 'Wallenstein', 'Washington', 'Weinstein', 'Weiss', 'Wellington', 'Wells', 'Williams', 'Wintle', 'Wittwer', 'Wolk', 'Wong', 'Woolworth', 'Wooten', 'Wright', 'Xe', 'Xee', 'Xi', 'Yanez', 'Yavinsky', 'Yeung', 'Yim', 'Yones', 'Young', 'Zalter', 'Zarabi']
#About 319 last names.

	# pick gender:
	# this also picks all relation language.
	gender = random.choice(["male","female"])
	if gender == "male":
		# all gender-specific titles here.
		firstname = random.choice(malenames)
		prefix = "Mr."
		manorwoman = "man"
		boyorgirl = "boy"
		pronoun = "he"
		thatisherdog = "his"
		thatshers = "his"
		thatshim = "him"
		relationtochild = "father"
		relationtospouse = "husband"
		relationtosibling = "brother"
		relationtoniece = "uncle"
		relationtograndchild = "grandfather"
		relationtograndfather = "grandson"
		relationtoaunt = "nephew"
		relationtofather = "son"
	elif gender == "female":
		#all gender-specific titles here.
		firstname = random.choice(femalenames)
		prefix = "Ms."
		manorwoman = "woman"
		boyorgirl = "girl"
		pronoun = "she"
		thatisherdog = "her"
		thatshers = "hers"
		thatshim = "her"
		relationtochild = "mother"
		relationtospouse = "wife"
		relationtosibling = "sister"
		relationtoniece = "aunt"
		relationtograndchild = "grandmother"
		relationtograndfather = "granddaughter"
		relationtoaunt = "niece"
		relationtofather = "daughter"
	else:
		error = "There is an error in the gender choosing code."
		return error
	pass
	#All non-gender specific information can go on this line.
	lastname = random.choice(lastnames)
	fullname = firstname + " " + lastname
		

	#Succinctly, this can be used to make a dynamic, random story. "This is " + character[1]+", "+character[7]+"  is great."
	#MAP
	# 0 is gender
	# 1 is full name
	# 2 is first name
	# 3 is last name
	# 4 is prefix
	# 5 is man or woman
	# 6 is boy or girl
	# 7 is pronoun
	# 8 is thatisherdog
	# 9 is thatshers
	# 10 is thatshim
	# 11 is relation to a child
	# 12 is relation to a spouse
	# 13 is relation to a sibling
	# 14 is relation to a niece
	# 15 is relation to a grandchild
	# 16 is relation to a grandfather
	# 17 is relation to an aunt
	# 18 is relation to a father
	character = [gender,fullname,firstname,lastname,prefix,manorwoman,boyorgirl,pronoun,thatisherdog,thatshers,thatshim, relationtochild, relationtospouse, relationtosibling, relationtoniece, relationtograndchild, relationtograndfather,relationtoaunt,relationtofather]
	return character
# End of create character
def chooseop():
        timer1 = random.randint(1,1000)
        for i in range(0,timer1):
                pass
        timer2 = random.randint(1,1000)
        pass
        pass
        pass
        pass
        num1 = random.randint(0,12)
        pass
        pass
        pass
        pass
        for i in range(0,timer2):
                pass
        g = random.choice(["a","m","s"])
        pass
        pass
        pass
        pass
        num2 = random.randint(0,12)
        if g == "a":
                ans = num1 + num2
                statement = str(num1) + " + " + str(num2) + " = "
        elif g == "m":
                ans = num1*num2
                statement = str(num1) + " * " + str(num2) + " = " 
        elif g == "s":
                if num1 > num2:
                        ans = num1 - num2
                        statement = str(num1) + " - " + str(num2) + " = "
                else:
                        ans = num2 - num1
                        statement = str(num2) + " - " + str(num1) +  " = " 
        else:
                return "error"
        amalgam = [ans,statement]
        return amalgam

#game begins here.
print("You are a leader of the people! What is your name?")
king = input()
print()
time.sleep(4)
print("Hello, Leader " + king + ". Your people need your help solving their math problems! Only you can solve all 100 problems!")
time.sleep(5)
print()
correct = 0
incorrect = 0
while True:
        time.sleep(1)
        print("ANSWERS CORRECT: ",end="")
        print(correct)
        time.sleep(.5)
        print("ANSWERS INCORRECT: ",end="")
        print(incorrect)
        time.sleep(.5)
        print()
        time.sleep(1)
        statement = chooseop()
        # statement 0 is answer
        subject = createcharacter()
        sub = subject[1]
        flavor = random.choice(['I have always been loyal to you, but I need your help."','everyone knows you are the best at math. How do I do this?"','I do not know if I can do this without your help!"'])
        print(sub + ': "' + king + ", " + flavor,end=" ")
        print()
        print()
        print(statement[1],end=" ")
        answer = input()
        print()
        try:
                int(answer)
        except:
                print("That answer does not seem to be a number. Perhaps you typed it wrong, Leader. Let's try helping someone else.'")
                print()
                time.sleep(3)
                continue
        if answer == str(statement[0]):
                print("Yes, that does seem like the correct answer. Great job!")
                print()
                correct += 1
                time.sleep(1)
        else:
                print("That answer is incorrect. Let's try another problem.")
                print()
                incorrect += 1
                continue
        if correct >= 100:
                print("You have solved 100 problems! You have proven yourself as a great leader and won the game!")
                print()
                input()
                break
        elif incorrect >= 100:
                print("You have gotten 100 problems incorrect. You are our greatest leader, please restart the game and work with a friend or mentor to help.")
                print()
                input()
                break
        else:
                        pass
                        print("Let's try helping another person!")
                        print()
                        time.sleep(1)