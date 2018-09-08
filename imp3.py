from nltk import word_tokenize, pos_tag
from nltk.corpus import wordnet as wn
from scipy.spatial import distance
from sklearn.cluster import KMeans
import numpy as np

def penn_to_wn(tag):
    """ Convert between a Penn Treebank tag to a simplified Wordnet tag """
    if tag.startswith('N'):
        return 'n'
    if tag.startswith('V'):
        return 'v'
    if tag.startswith('J'):
        return 'a'
    if tag.startswith('R'):
        return 'r'
    return None
 
def tagged_to_synset(word, tag):
    wn_tag = penn_to_wn(tag)
    if wn_tag is None:
        return None
    try:
        return wn.synsets(word, wn_tag)[0]
    except:
        return None
 
def sentence_similarity(sentence1, sentence2):
    """ compute the sentence similarity using Wordnet """
    # Tokenize and tag
    sentence1 = pos_tag(word_tokenize(sentence1))
    sentence2 = pos_tag(word_tokenize(sentence2))
    # Get the synsets for the tagged words
    synsets1 = [tagged_to_synset(*tagged_word) for tagged_word in sentence1]
    synsets2 = [tagged_to_synset(*tagged_word) for tagged_word in sentence2]
    # Filter out the Nones
    synsets1 = [ss for ss in synsets1 if ss]
    synsets2 = [ss for ss in synsets2 if ss]
    #print synsets1
    #print synsets2
    score, count = 0.0, 0
    fin = []
    # For each word in the first sentence
    for synset in synsets1:
        # Get the similarity value of the most similar word in the other sentence
        #print [synset.path_similarity(ss) for ss in synsets2]
        best_score = max([synset.path_similarity(ss) for ss in synsets2])
        # a = [synset.path_similarity(ss) for ss in synsets2]
        # s = 0
        # c = 0
        # for i in a:
        #     if(i is not None):
        #         s = s+i
        #     c = c+1    
        # Check that the similarity could have been computed
        if best_score is None:
            best_score = 0.0
        score += best_score
        count += 1
        fin.append(best_score)
    # Average the values

    ch = [1]*len(synsets1)
    #print distance.euclidean(ch,fin)
    score /= count
    
    #print score
    return fin, score



d3 = "Dear Local Newspaper @CAPS1, @CAPS2 our technology advance, so do are lives. Computers are a perfect way to better our way of life in ways that are benificial to us and future generations. The use of computers, and the @CAPS5 alone allow us to learn about the way of life in other places on @LOCATION4 talk to people faraway, and express ourselves. Computers give us a bright future. First many people, actually @PERCENT1 of the worlds population are generally stationary, and line in a local town or city environments. This is why computers are so helpful because they give @CAPS2 a way to research other places around the globe. @CAPS3 can create an interest in other cultures, and shape our opinions @CAPS2 @CAPS3 discover things about other places. From there, @CAPS3 can look at different topics in a wide spread point of view. In doing this @CAPS3 will connect to other ways of life. @CAPS2 philosopher and poet @PERSON1 state\" @CAPS3 learn about ourselves through the discovery of others.\" @CAPS4, another particularly handy function of the @CAPS5 through computers is @CAPS3 can communicate with people who live far away, when @CAPS3 couldn't visit otherwise. A @LOCATION2 study showed that actually @PERCENT2 of use of the computer is communication with sites like facebook or @CAPS9. A scientist in @LOCATION3, @PERSON3, says @CAPS3 @CAPS2 humans tend to enjoy communication because it gives @CAPS2 a sense of unity. This is why so many companies are realizing that sites like @ORGANIZATION2, @CAPS6, and @ORGANIZATION1 are gaining in popularity.\" And this is true. It is enjoyable to @CAPS7, talk, or email others. Without computers, this couldn\'t be possible. Lastly, computers give us the chance to express our ideas like never before. Now, stars aren\'t only made in @LOCATION1, but now you can make yourself famous on @CAPS8 or @CAPS9. Just ask @PERSON2, who\'s voice reached out and caught the attention of a major record company. Now, everyone knows his name and listens to his music. Like @PERSON2, the more wordy folks can express themselves by blogging their opinions. \" About half of computer use, \" says @CAPS1 to computer weekly, @PERSON4,\" is using blogs and videos to state one\'s ideas.\" @CAPS3 can persuade others to think @CAPS2 @CAPS3 do and discover thngs that @CAPS3 have discovered. Self-expression is very important to society, and this is why computers have such an affect on people. @CAPS2 it is clear, computers have a positive affect on people and society. They allow us to learn about faraway places, communicate with others, and inspire the world around us with our ideas. Welcome to the future."
d4 = "Dear Local Newspaper: @CAPS1 you know that over half our nation own home computers? Recently, though, some experts have been concerned whether or not computers benefit society. I have been asked to state my opinion and I believe computers have a positive effect becuase, they are mandatory for work, allow online socialization, and expand traveling. After reading this, I am sure you will agree. Firstly, computers are mandatory to have for work and @ORGANIZATION1. Students keep their essays, study guides, and home work updates on files in the @CAPS5. Offices would not be able to function @CAPS8 computers; workers rely on the internet email system. An interviews with a student from @ORGANIZATION1 says, \"I use my @CAPS5 for everything; I would not survive the workload @CAPS8 @CAPS3.\" @CAPS2 asked why, he replied, \"@CAPS3 keeps everything organized, and is an easier way to research topics.\" A lawyer said, \"You can not support a client if you don't have the right tools, and a @CAPS5 is on @MONEY1 those tools.\" @CAPS4, @CAPS8 computers offices would crumble and students grades would drop. Could you imagine writing a newspaper @CAPS8 a @CAPS5? Secondly internet access allows people to meet new people. Many websites such as '@CAPS6' and '@CAPS7' allow people to reconnect with old friends, and make new ones. @PERCENT1 @MONEY1 the nation owns accounts on socializing websites, and @PERCENT2 @MONEY1 the nation says their friend groups have expanded to the groups (according to a poll taken). A psychologist explains, \"Some people are too shy to meet new friends in person; online bloom.\" @CAPS8 internet, citizens @MONEY1 @LOCATION1 would know little about other countries' people. My next reason, however is even greater. Lastly, @CAPS8 internet, people would do for less traveling. Internet allows citizens to research places they would like to visit and buy transportation to their destination. @CAPS3 also is an easy and effective way @MONEY1 booking where the tourist shall stay. Apoll taken by @ORGANIZATION2 airports shows that @PERCENT3 @MONEY1 the travelers book their flights online and @CAPS8 online ticketing 'the wait to book your flights would be unbearabley long; or stop travelers completely' (quote from a worker). My people and I went to various airports and train stations across the country and interviewed @NUM1 people each. We inquired about how the bought their tickets and @PERCENT4 @MONEY1 them said online. \"@CAPS9 do you mean, how? On the internet @MONEY1 course! no one could get anywhere if we stood in lines all day!\" said a person interviewed. Airports make @MONEY1 for the @LOCATION2 government, and @CAPS8 internet less people would travel. There for, computers are mandatory. Computers have a positive effect on owners; since they allow easy organization and research, online socializing and better ways @MONEY1 booking transportation. @CAPS8 computers internet access, our business would crumble, then the economy would follow. I know you agree with me."

d5 = "Dear Local newspaper, @CAPS1 you have a computer at home you enjoy? Computers are a big thing now in life, they help with many things. Such as staying organized, studies, and even entertainment. These are the three topics I will focus on, because I @CAPS1 believe that computers are useful and people use them a help to make life a lot more easy. Let me start by saying: \"I am a man who enjoys computers, as a way to talk to friends, listen and search music, watch videos on youtube, get school work done, and much more! Although, on main point is it helps me stay orginized. I can make many folders to store my work in, rather then losing or spilling something on the paper if I wrote it out. I can have my music, homework, projects, does work, videos, pictures, and much more saved and orginized so I know where it is everytime I go to find it. There can be no more, \"my dog ate my homework\" excuse. Moving on to the next topic. As I mentioned you can save work onto your computer, you can add without earasing as well, the work becomes neat and perfect everytime. So when you teacher is grading on neatness no worry. You can also look up information on any topic you are working on in class witch alows you to get. More information, the better the grade. Spelling is not a factor now, because your computer tells you when a word is spelt wrong. It even gives you suggestions on how to spell the word by underlining it with a red squigle line. This really helps because a lot of people have hard times with spelling. You can even get @CAPS2 to play a book you are reading, witch helps you learn new words that you @MONTH1 not have knew how to sound out. Teachers can even post notes on school websites of homework, when projects are @CAPS1, ext. No more, \"I didn't know/remember what was homework/project due. Lastly, entertainment is the biggest thing with computers. People go on every day uploading videos, pictures, blogs, and just about what ever they want. Games are played on computers by younger kids, just learning, while older kids are enjoying playing maze, driving, shooting, adventure, and much more types of games. Just about everyone using a computer knows of some chat website in witch they use to communicate with any one. Myspace, facebook, twitter, and so much more are used by people to talk, express how they feel to everyone/to just let it out), show love to someone, send birthday wishes, to @CAPS1 what ever. Those are endless possibilities at entertainment on a computer. Without a dobt, no more, \"I\'m bored\". @CAPS1 you use your computer to @CAPS1 anything like this? If so you must enjoy it. People use computer for every thing from work to expressing feelings. Now what side are you at?"

d6 = "Computers are used world wide everyday, and most of the time @CAPS2 is used for a good reason. Computers help out by making @CAPS2 possible to get all the info you want, like for a trip. @CAPS1 you wanted to go to a close but fancy restaurant you @MONTH1 use a computer so you know how far. Computers also help out, making @CAPS2 possible to talk to friends that you haven't seen for years. @CAPS2 is also great way to meet new people. Let's say you are really stressed at work or school and you forget your book, you can usually bring @CAPS2 up on the computer and do @CAPS2 there. First, computers help out with traveling, sight seeing and lots more. When you travel, dont you want to know everything? And the biggest detail you want to know is the cost and the computer can usually give you a close to exact price for everything. Now that help's out a bunch when your traveling the world. And also when your site seeing you usually want to find either the most amazing or romantic spot were you are. And @CAPS1 you type in \"the most romantic spot in somers\" @CAPS2 should come up with a bunch of spots. So dont drive to miles just to get a map or brochure, use your computer and print one off. Second, @CAPS1 there was a friend you haven't seen in years and you want to talk, you can go on the computer. The computer helps in so many ways @CAPS2 could even tell you were this person lives and you could surprise visit him/her. When your on the computer, you can even meet new friends and have conversations with them. and even meet them someday. And @CAPS1 you and that new friend get along then mabey you and that person could be best friends. So @CAPS1 you haven't seen or talked to someone in a while that you knew use the computer to have a chat. Third, say your teacher or boss yelled at you today and no one has been nice to you all day and you forget your homework book or paperwork. Were do you go? the computer, @CAPS2 can bring most any paper work or work book you need to get the job done. @CAPS1 you forgot your homework book, you dont want to get a falling grade. on this homework. So you go to your computer from there. And @CAPS1 you forgot your paper work, and @CAPS1 you didn't finish this project for work tonight you would be fired, you could just go on the computer, find the work and finish @CAPS2. Also save your job. So that why computers help out so much in this lifetime. Last, that is why in this lifetime you need computers. They help us with our vacation trips. They help with conversation with old friends we haven't seen forever. Also they help with your school and job work. At least @PERCENT1 of our population use computers every day and with out them our society would colaps/ @DATE1. So think about the decision you are making and @CAPS1 @CAPS2 will benefit our society or make our society @DATE1 to its knees."

d66 = "Dear, local newspaper, @CAPS1 you like computers? I @CAPS1, computers help you learn about all kinds of things. Plus computers let you chat to people on there computer even if you can't call them. Another reason why I love computer are because when I have to write a project I can just type it!!! Computers make eveything easier. So, @CAPS2 consider liking computers. Initially, imagine you have a project due in two days. Your mom can't drive you to the library and you have no information on the subject. But hey, don't you have a computer. You can use the computer to lock up your subject and a @CAPS3 different websites will come speed quick to your screen. Most of then will help you learn about the subject and then you have time to finish it and hang out with your friends. Secondly, @CAPS4 @CAPS5!!! you frogot what page of the book your suspose to read. Also you lost all your friends contacts. Not to fear super duper computer is here. You can email or chat to your friends online and see what pages to read and get there phone numbers back. Did you know @PERCENT1 out of @NUM1 People said that the chat & email programs are @CAPS6 because they can contact friends, family, and co-workers. Finally, you can type your essay on the computer. Writing a @NUM2 paragraph essay takes to long, so use your computer to help you out. Go to microsoft office and type your essay. Computers make writing an essay really easy. @PERCENT2 out of @NUM3 people said they like typing on the computer more then writing it on @CAPS7. in conclusion, Computers are @CAPS6 tecnollogy when you have to chat to someone. Also when you learn about something. Another reason why computers are @CAPS6 is because you can type essays & papers, @CAPS8, @CAPS2 change you @CAPS10 of computers are bad to computers make us @CAPS11!"

d7 = "Dear local newspaper, @CAPS1 opinion on the effects computers have on people is a positive effect. Three main reasons are that people learn more about cultures, places, and some people work online. @CAPS1 first reason why computers have a positive effect on people is because they help you learn about cultures around the world. Learning about cultures is very important because if people travel they need to know how they can respect each other. @CAPS1 second reason why computers have a positive effect on people is because they help you learn about places around the world the world. Learning about places is very important because you could get lost. It also helps you by telling you which places are famous to visit. @CAPS1 third reason why computers have a positive effect on people is because some people find jobs online. Other people work online. This benefits people in a positive way. In conclusion computers have a positive effect on people because its helps people learn about cultures, places, and jobs around them."

d77 = "Dear readers, People around the world are starting to use computers now more, often, but theirs also people that dont agree that it benefits society, @CAPS1 not one of those people. I agree that this benefits society. One reason why I agree is because sometimes theirs teens and even adults that can chat online with their friends if they cant contact them in any other way. Another reason is because in all school teacher give their students project to do over vacation or weekends, for the projects they can look for information in the computer. The last reason is because computers can give ability to learn more about things they didnt know before. In my opinion I agree with computers benefiting society. Teens, kids and even adults would like to talk with their friends so they can get on the computer and chat with them if theirs no other way to contact them, @CAPS2 easy. You only have to @NUM1) get in the computer, @NUM2) get into a site were you know your friend might be @NUM3) log in or register in if you never been into that site @NUM4) last but not least look @NUM4 your friend to chat will teachers always give their students work for example like projects. Kids also do projects on weekends or vacation and so you dont have to go to a library to check out a book you could always get on the computer and look for the information you need their. Computers give you abilitys to learn information you didnt know before for example if your bored and you dont got nothing to do get in the computer and look up information about things like nature, books your looking for etc. I agree with computers benefiting society but not everyone, @NUM3 reason why I agree is kids can chat online with their friends, look up information for projects and find information they never knew about, what do you think @CAPS1 I right or wrong."

d8 = "Dear @CAPS1, I, agree that computers are benefits society. The computers have positive effect on people like hand-eye coordination. I helps you learn about other country religios, and other thing. You can communicate, meet other people, and chat tru computers. Another positive fact about computer is that you can find all the information you need and fast. In other words is that computer help a lot of people."

d88 = "Dear: @CAPS1 @CAPS2 @CAPS3. My name is @PERSON1 and I am concernd about people around the world are use computer is to much during the day. Some compute's are bad because there are glitche\'s in the computer and every one has a myspace and myspaces has a viries and it leaves a vires in your computer and your computer shut\'s down or goes slow. Also people can hack your computer and you cant find out about and every thing that was on your computer can go around the world. People can kno your most secread\'s and more. Finly you can get caught macking movies on your computer and go to jail and your business will be out."

d9="I think computers are good because you can talk to your friends and family on the computers. People needs computers to look for a job. Some people spend to much time on the computers then on homework people need to stop."
sentences = [d3, d4,d5,d6,d66, d77, d7, d88, d8, d9]
focus_sentence1 = "Dear @PERSON4, I strongly believe that use of computer is beneficial to the community. One reason I feel this way is that computers can improve hand-eye coordination and other skills. These computers provide access to games helpful in @ORGANIZATION2 training. In fact, @ORGANIZATION2, in @LOCATION1, @CAPS1, just began using these games as part of their training this @DATE1. Instructors report that @ORGANIZATION2 skills in trainees and students are far better than in years past. Additionally, computer games can improve reflexes. Two years ago, a man named @PERSON3, @NUM1 years old, fell onto the train tracks just as a train was coming by. Through extra-ordinary reflexes he managed to leap out of the way, saving his life. When asked how he did @CAPS5, he said he had been playing computer games since he was @NUM2 years old. These games also make you more intelligent. The @ORGANIZATION1's @DATE2 study reports that brains were @PERCENT1 more active after use of computers. The researchers achieved this data by attaching electrolytes to the patient's brain both before and after using the computer. @CAPS5 is for these reasons that computers improve hand-eye coordination and other skills. Another reason for why computers are beneficial is that they allow you to talk online. They even allow you to communicate with your family who live far away, strengthening your relationships. I recently got back in touch with my cousin who moved to @LOCATION3. Letters were too expensive and took too long, but email and skype provide us with a great alternative. These computers also improve social skills. @PERSON1, resident here in town, says, \"I love using computers because I can talk to my friends whenever I want, and I feel like @CAPS5 really helps us communicate.\" Who wouldn't love a machine that provides a service like that? These computers can even improve your mood. In a test done by @ORGANIZATION3 in @DATE3, @NUM3 people were put in seperate rooms with personal computers for @NUM4 hour. Afterwards, @PERCENT2 said they felt an improvement in their mood. Computers are great because they allow you to talk online. Finally, computers allow you to learn about other places. Virtual tours are becoming more and more common today. Infact, at @CAPS2.org, you can take virtual tours of over @NUM5 different countries, including @LOCATION5, @LOCATION4, @LOCATION2, and @LOCATION6. You can also learn about other cultures and their traditions through online videos at youtube.com and articles at wikipedia.org, the free encyclopedia. You can even learn new recipes. Celebrity chef extraordinare @PERSON2 not only posts all her recipes online at mstewart.com, but she even finds some of them! In a recent interview by @CAPS3 magazine, when asked where she's found some of her best recipes, including her famous @CAPS4 chocolate cake, @PERSON2 admits she found most of them online, saying, \"@CAPS5's a powerful resource that more people should use. Al @CAPS6 currently owns the world's best cookbook!\" @CAPS5 is because of this that computers allow you to learn about other place. Thank you for your time, and I hope you take what I have said into consideration. @CAPS5 is for all of these reasons I strongly believe computers are beneficial to the community."

focus_sentence2 = "Dear @CAPS1 of the @CAPS2 @CAPS3 @CAPS4, computers are a wonderful tool and they bear many positive impacts on society first, computers have created numerous @CAPS2 forms of communication. Also, they have enable us to create a @CAPS2 age in research. In addition, computers have given us amazing @CAPS2 ways to entertain ourselves computers have a incredibly positive effetct on people. One reason why computers have such a positive effect on humans, is that we have developed many @CAPS2 ways to communicate with people all over the world. First, one fantastic program such as @CAPS5 (instant messaging) has given us the amazing ability to hold a conversation with one or more people any where in the world, and be able to respond within an instant. In a recent survey @PERCENT1 of people said that they prefer instant messaging over any other type of communication beside face to face talking, second, most computers come with webcams built in now, so you can actually see the person you are communicating with. I had friend move recently, and we are able to see what each other are doing and remain friends even though we don't live in the same town, and I'm sure a similar experience has occured to you or someone you know. Finally, the popular program of facebook has changed communication forever. People can now see things go on in your info whereever want. Although some it has a wonderful computers have established incredible ways of communication. A second reason computers positively import people is that they have created a numerous research. One example would be our phenomenon search engine, google. Google to almost everything with help people in finding schools now use computer resources such us @CAPS6 which allow in research to the fact that there is so much availbale on the. In addition, computers have created many opportunities for people to learn more because of the billions of web you in existance studies have shown that @PERCENT2 of people have found a website conataining information relevant to their research that was than a book. Computer are the reason that research has contuined to thrive and @CAPS2 continue to be made. Finally, computers have established amazing @CAPS2 entertainment for people of all ages. First, video websited such as youtube have created a place for people to watch music videos and creative films just to enjoy themselves. If you can't get tickets to a concert you want going online to watch music videos by that person is a much cleaper alternative, second, jaming websites are a less expensive, but if you go online you can play similar games at no charge. Finally websites with appropriate funny stories posted on them are a fantastic way to get the laughter of a comic, without leaving your couch wouldn't you prefer to stay home, rather than going out when it isn't necessary? computers are an incredible way to achieve quick, un expensive entertaiment in todays economy. In conclusion, computers impact proper in many positive ways. they're established now forms of communication, research and entertainment that will forever change society. Therefore, I invite you to join me to demonstrate the icrredible strenght of computers."

focus_sentence3 = "Dear local newspaper, I has come to my attention that many of us disagree on weather computers have a negative or positive effect on people. I believe that computers do not benefit society. Many people in today's modern world spend way to much time on the computer when they could be exercising, spending time with family and friends, and enjoying nature. Read on and I am sure you will agree. First of all, computers are becoming a problem in society because they interfear with our physical well being. The @LOCATION1 is continuingly growing. Not in our population but the size of our people! According to a recent survey @NUM1 out of every @NUM2 people in the @LOCATION1 are overweight or obease. \"The main culprit of the @ORGANIZATION2's percent of obeasity is not over eating it is actually electronics! Especially things like computers.\" said @PERSON1 a surgean at @ORGANIZATION1, after dealing with a severe case of obesity. Obesity is not a hard thing to get rid of. All we have to do is instead of sitting for hours staring at a screen. America needs to get outside! It can be as simple as riding a bike or taking your dog for a walk. Whatever you do just get off your computer and go outside or the gym for exercise! Secondly, computers interfere with family and friends. I know from personal experience that parents hate it when their kids will miss family dinner or won't go out with their friends because they \"need\" to finish the next level on their game or they \"need\" to look something up on the internet. Family and friends should be a very important thing in your life but unfortunatly, for most people it is not. Psycologist, @PERSON2 has discovered that overall, having family and friends that you can count on beside you will make you a much happier more enjoyable person.\" @CAPS1 eliminating computers from our lives we will create a happy and more pleasent society for the people of the @LOCATION1. Doing everyone a favor. Furthermore, if we cut back on our hours on the computer we will have a better chance to expeirence the wonder's mother nature has to offer us. Most people don't realize how much they are missing @CAPS1 not going outside. There are amazing things, right in your own backyard, that you will probably never get to expeirience because you are too addicted to playing on the computer. @NUM3 years ago people were able to function fine with out computers so we should be able to too. @PERCENT1 of people have never even been camping! So next time you feel like spending another @NUM4 hours on the computer, take a walk and I'm sure you will be amazed at what you find outdoors. In conclusion, computers do not benefit society. They just keep people away from going outside, enjoying nature and spending time with family and friends. I hope I have convinced you to see my side of the argument and thank you for your time."

focus_sentence4 = "Dear readers, On the current debate of the effects of computers, I believe they strongly benefit all people. For example on some computers a business software can be incorporated, allowing a meeting to be help over the computers. Not only is it convienent, but this saves money. Also, computers come with built in programs that can help keep track of you expenses. These are simple and save lots of time. Plus, computers also help you stay in touch with friends. Even if they are @NUM1 miles away you can click a button and have a live video chat! First off, the business software on new computers are out of this world. You can make a brochure of sales and expenses, all with an easy stroke on the mouse. This is a cheaper and greener way of presenting ideas. Furthermore, on the computer you and all you clients can hold a conference call. Doing this allows you to relax and multitask while your computer is feeding you coverage of the call in crystal-clear sound. Normally a phone would have to be glued to you ear but now you hands free. Another time where computers are handy is at tax time. Tired of running around your house to find you car bill from three months ago? Well, with a spreadsheet software like @ORGANIZATION1, taxes can be calculated in along with their name, so when you take the taxes to tax consultant, everything is organized. Using these tools cut down an stress and leaves you less frustrated. And even better, you can buy a tax program for you computer, so you never have to leave your couch! Think about, paying somebody to count your taxes year after year, when you can save a fortune and do it yourself. Above all, computers help you connect with old friends who have moved away or parted ways earlier in life. Now, the internet contains many social networking sites, such as @CAPS1, @CAPS2, and @CAPS3 where you can reunite with lost pals. These networks also offering access to photosharing and chat, so everybody can see how your family is and vice versa. Along with this is video chatting, where you can have face to face conversation with somebody even on the other side of the world. This is totally private, so it isn't dangerous to say names of family members or their locations. The internet truly is an amazing tool! To conclude, the internet holds a very strong role in our daily lives. Not only can we see who man the @ORGANIZATION2 game, but it also has interactive business softwares as well. Never again will work be so difficult. Also, the computer has programs to help you manage expenses, keeping you on top of your game. Finally, it is also helpful for all the tools that can be used to interact with friends thousands of miles away. I believe the computer is critical for success and happiness in life. It's a new age, let's adapt to it."
# print sentence_similarity("Smit is going home. His house is in Gandhinagar.","Smit is going to his house in Gandhinagar.")
# print sentence_similarity("Smit is going home. His house is in Gandhinagar.","Lionel Messi is from gandhinagar same as Smit.")
# print sentence_similarity("Smit is going home. His house is in Gandhinagar.","Lionel Messi is from gandhinagar but he hates that place.")
# print sentence_similarity("Smit is going home. His house is in Gandhinagar.","Lionel Messi is the greatest football player ever.")

mat = []
for sentence in sentences:
    #print "Similarity = %s" % (sentence_similarity(focus_sentence, sentence))
    fin, score1 = sentence_similarity(focus_sentence1, sentence)
    fin, score2 = sentence_similarity(focus_sentence2, sentence)
    fin, score3 = sentence_similarity(focus_sentence3, sentence)
    fin, score4 = sentence_similarity(focus_sentence4, sentence)
    
    avg = (score1 + score2 + score3 + score4)/4
    print avg
    #mat.append(fin)

#mat = np.array(mat)

#kmeans = KMeans(n_clusters=3,n_init=20, random_state=0).fit(mat)

#print kmeans.cluster_centers_
#print kmeans.labels_
