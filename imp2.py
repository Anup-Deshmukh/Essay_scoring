from nltk import word_tokenize, pos_tag
from nltk.corpus import wordnet as wn
from scipy.spatial import distance

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
        a = [synset.path_similarity(ss) for ss in synsets2]
        s = 0
        c = 0
        for i in a:
            if(i is not None):
                s = s+i
            c = c+1    
        fin.append((s/c))
        # Check that the similarity could have been computed
        if best_score is None:
            best_score = 0.0
        score += best_score
        count += 1
    # Average the values
    ch = [1]*len(synsets1)
    print distance.euclidean(ch,fin)
    score /= count
    return score



d3 = "Dear Local Newspaper @CAPS1, @CAPS2 our technology advance, so do are lives. Computers are a perfect way to better our way of life in ways that are benificial to us and future generations. The use of computers, and the @CAPS5 alone allow us to learn about the way of life in other places on @LOCATION4 talk to people faraway, and express ourselves. Computers give us a bright future. First many people, actually @PERCENT1 of the worlds population are generally stationary, and line in a local town or city environments. This is why computers are so helpful because they give @CAPS2 a way to research other places around the globe. @CAPS3 can create an interest in other cultures, and shape our opinions @CAPS2 @CAPS3 discover things about other places. From there, @CAPS3 can look at different topics in a wide spread point of view. In doing this @CAPS3 will connect to other ways of life. @CAPS2 philosopher and poet @PERSON1 state\" @CAPS3 learn about ourselves through the discovery of others.\" @CAPS4, another particularly handy function of the @CAPS5 through computers is @CAPS3 can communicate with people who live far away, when @CAPS3 couldn't visit otherwise. A @LOCATION2 study showed that actually @PERCENT2 of use of the computer is communication with sites like facebook or @CAPS9. A scientist in @LOCATION3, @PERSON3, says @CAPS3 @CAPS2 humans tend to enjoy communication because it gives @CAPS2 a sense of unity. This is why so many companies are realizing that sites like @ORGANIZATION2, @CAPS6, and @ORGANIZATION1 are gaining in popularity.\" And this is true. It is enjoyable to @CAPS7, talk, or email others. Without computers, this couldn\'t be possible. Lastly, computers give us the chance to express our ideas like never before. Now, stars aren\'t only made in @LOCATION1, but now you can make yourself famous on @CAPS8 or @CAPS9. Just ask @PERSON2, who\'s voice reached out and caught the attention of a major record company. Now, everyone knows his name and listens to his music. Like @PERSON2, the more wordy folks can express themselves by blogging their opinions. \" About half of computer use, \" says @CAPS1 to computer weekly, @PERSON4,\" is using blogs and videos to state one\'s ideas.\" @CAPS3 can persuade others to think @CAPS2 @CAPS3 do and discover thngs that @CAPS3 have discovered. Self-expression is very important to society, and this is why computers have such an affect on people. @CAPS2 it is clear, computers have a positive affect on people and society. They allow us to learn about faraway places, communicate with others, and inspire the world around us with our ideas. Welcome to the future."
d4 = "Computers are used world wide everyday, and most of the time @CAPS2 is used for a good reason. Computers help out by making @CAPS2 possible to get all the info you want, like for a trip. @CAPS1 you wanted to go to a close but fancy restaurant you @MONTH1 use a computer so you know how far. Computers also help out, making @CAPS2 possible to talk to friends that you haven't seen for years. @CAPS2 is also great way to meet new people. Let's say you are really stressed at work or school and you forget your book, you can usually bring @CAPS2 up on the computer and do @CAPS2 there. First, computers help out with traveling, sight seeing and lots more. When you travel, dont you want to know everything? And the biggest detail you want to know is the cost and the computer can usually give you a close to exact price for everything. Now that help's out a bunch when your traveling the world. And also when your site seeing you usually want to find either the most amazing or romantic spot were you are. And @CAPS1 you type in \"the most romantic spot in somers\" @CAPS2 should come up with a bunch of spots. So dont drive to miles just to get a map or brochure, use your computer and print one off. Second, @CAPS1 there was a friend you haven't seen in years and you want to talk, you can go on the computer. The computer helps in so many ways @CAPS2 could even tell you were this person lives and you could surprise visit him/her. When your on the computer, you can even meet new friends and have conversations with them. and even meet them someday. And @CAPS1 you and that new friend get along then mabey you and that person could be best friends. So @CAPS1 you haven't seen or talked to someone in a while that you knew use the computer to have a chat. Third, say your teacher or boss yelled at you today and no one has been nice to you all day and you forget your homework book or paperwork. Were do you go? the computer, @CAPS2 can bring most any paper work or work book you need to get the job done. @CAPS1 you forgot your homework book, you dont want to get a falling grade. on this homework. So you go to your computer from there. And @CAPS1 you forgot your paper work, and @CAPS1 you didn't finish this project for work tonight you would be fired, you could just go on the computer, find the work and finish @CAPS2. Also save your job. So that why computers help out so much in this lifetime. Last, that is why in this lifetime you need computers. They help us with our vacation trips. They help with conversation with old friends we haven't seen forever. Also they help with your school and job work. At least @PERCENT1 of our population use computers every day and with out them our society would colaps/ @DATE1. So think about the decision you are making and @CAPS1 @CAPS2 will benefit our society or make our society @DATE1 to its knees."
d5 = "Dear local newspaper, @CAPS1 opinion on the effects computers have on people is a positive effect. Three main reasons are that people learn more about cultures, places, and some people work online. @CAPS1 first reason why computers have a positive effect on people is because they help you learn about cultures around the world. Learning about cultures is very important because if people travel they need to know how they can respect each other. @CAPS1 second reason why computers have a positive effect on people is because they help you learn about places around the world the world. Learning about places is very important because you could get lost. It also helps you by telling you which places are famous to visit. @CAPS1 third reason why computers have a positive effect on people is because some people find jobs online. Other people work online. This benefits people in a positive way. In conclusion computers have a positive effect on people because its helps people learn about cultures, places, and jobs around them."
d6 = "Dear @CAPS1, I, agree that computers are benefits society. The computers have positive effect on people like hand-eye coordination. I helps you learn about other country religios, and other thing. You can communicate, meet other people, and chat tru computers. Another positive fact about computer is that you can find all the information you need and fast. In other words is that computer help a lot of people."
d7="I think computers are good because you can talk to your friends and family on the computers. People needs computers to look for a job. Some people spend to much time on the computers then on homework people need to stop."
sentences = [d3,d4,d5,d6,d7]
focus_sentence = "Dear Local Newspaper, I believe that computers are an extremely useful tool in society. It helps people learn new things about different cultures. Also, it lets you communicate with friends and family through the internet, for example, using facebook or @CAPS1. Finally, it provides an accurate research tool for school projects, or interviews. First, learning about different cultures helps the world stay together. For example, here, we learn @CAPS2 and @CAPS3. Each class teaches us to respect more and more of this culture. However, some people don't have the chance to get this land of education, so they turn to the internet. If the computer didn't exist, we might not know about the lifestyle @NUM1 mi away from us. We wouldn't know if their lifestyles are extremely difficult or luxurious. Also, we wouldn't know if we could help them or not. For example, the earthquake in @LOCATION1 which. It's one step closer to world peace no more war or conflicts. Secondly, the computer helps you communicate to friends and family for in the world. I remember one time I was mailing my family friends who was in @LOCATION2, risking his life. I knew he couldn't come back to town, so I started to email him, and video chat with him. Whenever I saw his face, I knew that everything was okay. I don't know how I would have without the internet. Other ways lived you could as. Also, just communicating with friends! internet sites, like extremely useful. Finally, you use the computer for educational use. For example, research projects, study tools and essays. Whenever that a research is the internet. This extremely reliable and accurate. However that some of the websites are fake, which is easy to great research to use for school projects. Also, I know many teachers in my school have a blog or page where they put their @CAPS4 on, study links, and handouts, just in case we lose them. Whenever there is a test coming up, my @CAPS2 teacher, @CAPS5 would have links on her go to help use study. Also, is another website that helps us study for vocab. It also has many games that and learn our vocab words. As you can see, the computer helps us in our daily use and makes a positive impact on our society. From educational purposes, to learning cultures and socializing with friends it helps us get through life. As very successful newspaper and people, I assume you will understand how much the computer has made a positive effect in society."

# print sentence_similarity("Smit is going home. His house is in Gandhinagar.","Smit is going to his house in Gandhinagar.")
# print sentence_similarity("Smit is going home. His house is in Gandhinagar.","Lionel Messi is from gandhinagar same as Smit.")
# print sentence_similarity("Smit is going home. His house is in Gandhinagar.","Lionel Messi is from gandhinagar but he hates that place.")
# print sentence_similarity("Smit is going home. His house is in Gandhinagar.","Lionel Messi is the greatest football player ever.")

for sentence in sentences:
    print "Similarity = %s" % (sentence_similarity(focus_sentence, sentence))
    print
