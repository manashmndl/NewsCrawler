stanford_classifier = 'D:\StanfordParser\stanford-ner-2015-12-09\classifiers\english.all.3class.distsim.crf.ser.gz'
stanford_classifier2 = 'D:\StanfordParser\stanford-ner-2015-12-09\classifiers\english.muc.7class.distsim.crf.ser.gz'
stanford_ner_path = 'D:\StanfordParser\stanford-ner-2015-12-09\stanford-ner.jar'

news_t = "Estelle Mossely celebrated her 24th birthday in style by punching her way into the history books as she became the first Frenchwoman to win Olympic boxing gold on Friday.Mossely also saw her fiance Tony Yoka battle into the mens super-heavyweight final less than an hour earlier and the pair plan to soon marry-making it a particularly special 2016 for Frances latest heroine.France is enjoying its best Olympics in boxing with the possibility of two more gold to come at the weekend for Yoka and Sarah Ourahmoune.Yoka was watching from the stands, still in the red vest he had fought in and with a white towel around his neck. He wiped away tears as Mossely edged a nervy split-points decision 2-1 over Chinas Yin Junhua in their lightweight clash.He then joined in as a small but vocal contingent of French staff and fans serenaded Mossely with happy birthday.She said that gold made her feel complete.Its a lovely birthday present. It is a beautiful birthday present and it is fitting after all of these years of training and studying, she said.I am very, very honoured to have won this gold medal and to be the first woman to win for France.Mossely is now desperate to see Yoka complete a perfect Games for the lovebirds.We have two parts of a contract and he has the second part in his hands. What can I say? Its just good for us.Mossely grabbed the initiative from the first bell but was down on the judges scorecards and in danger of seeing her birthday ruined.I spoke to my coach and he said, Youve trained hard for this, youre setting a good pace, you have good cardio, and he urged me on, she said.So from there it was just all instinct, trying to give more and more and more. And it worked.Mossely was the deserved winner having been the aggressor in the opening exchanges and to the very end of the bout against Yin, who was in fits of tears later when she collected her silver medal.ON PODIUM IN SLINGThe French boxer began to turn the tide of the fight when she rattled Yin at the end of the second with a fierce right that catapulted the Chinese back towards her own corner.Mossely was again on the attack at the end of the third, one left-right-left combination stunning the Chinese.And the Frenchwoman came out all guns blazing at the start of the fourth and final round-as Yoka bellowed his support and jumped up and down.Mossely had eased into the final without breaking sweat after Russias Anastasiia Beliakova dislocated her left elbow in the first round of their semi-final on Wednesday.The Russian was rushed out of the arena in tears and in a wheelchair, but returned to pick up her bronze on the podium, her arm in a sling and getting a huge ovation.Its always very pleasant to have an Olympic medal around your neck but of course I was coming here for a medal of a different colour. Unfortunately what happened has happened but Im very happy to have an Olympic medal, said Beliakova.Womens boxing-there are three weight categories-made its debut at the London 2012 Games but the lightweight champion there, Irelands Katie Taylor, made an early exit from Rio.Mira Potkonen of Finland, who beat Taylor, took home the other bronze medal."

text_t = "Manchester United manager Jose Mourinho pledged to shape his team around Paul Pogba after the France midfielder made a successful Old Trafford return in a 2-0 win over Southampton. Pogba played the whole game as Zlatan Ibrahimovics brace sank Southampton on Friday, a week after returning to United from Juventus in a world-record 89 million pound (105 million euros, $116 million) transfer. Despite playing in a midfield holding role, Pogba got forward well, making a total of four attempts at goal, and Mourinho said that he was determined to give the 23-year-old the freedom to play his natural game. Asked what instructions he had given Pogba, Mourinho replied simply: Play. He added: I dont know which position he played. For a player to play with the freedom he has, we have to build a certain organisation around him. He has to play with freedom. The last 10 minutes, 2-0, now (you need) more discipline, more tactical organisation, but this is the kind of guy that has to play free. Pogbas second debut, four years on from his last United appearance, got off to an embarrassing start when he produced an air-kick in midfield, but Mourinho was delighted by the way he regained his composure. I think he was fantastic. His first action was bad. He loses an easy ball and gives a counter-attack and a first free-kick to the opponent, Mourinho said.(But) you can see even more the ego, the personality. Hes so comfortable in the skin of a star, so confident, the way he plays. For 10 days work, first match of the season, not even 10 minutes of a friendly, I think he played phenomenal. Mourinho also reserved words of praise for Pogbas midfield partner Marouane Fellaini. Fellaini became a figure of derision under Mourinhos predecessors David Moyes and Louis van Gaal, but the United manager said that he had worked hard to build up the Belgium internationals confidence. PUEL REGRETSMaybe a simple phone call can make a difference, said the Portuguese, whose side provisionally went three points clear at the Premier League summit. A player that was feeling he was not loved. A player that when the market opened, everybody was saying he was leaving and was not a player for me. Maybe a simple phone call the day after my presentation as Man United manager changed a lot because I told him: Forget everything you read. With me, you dont leave, for sure. Then I think the more organised the team play, the easier for the players to feel confident. Hes playing well, with (Michael) Carrick, with (Ander) Herrera, with Paul. I think hes full of confidence, but I have so many good players. I arrived in the dressing room after the match and I was happy, and I became sad. All the other guys were there in their nice Paul Smith suits-Carrick, Memphis (Depay), (Phil) Jones-that I dont select. Ibrahimovic opened the scoring with a towering header from Wayne Rooneys cross in the 36th minute and made it 2-0 from the penalty spot early in the second half after Jordy Clasie tripped Luke Shaw. The Swedish striker, who was making his home debut, has now scored four times in three United appearances. Southampton created a few opportunities prior to falling behind, with Shane Long threatening twice, and manager Claude Puel lamented his sides failure to take their chances. We finish this game with a lot of regrets because we had many situations, said the Frenchman. Puel has introduced a new system featuring a diamond midfield, but he downplayed the significance of the tactical change. The system is not the most important thing. The most important thing for us is to play football, he said. When you play good football, we can make good opportunities. Its important to play and to believe in our potential. This is the most important thing."

from NLP.CustomNERTagger import Tagger
from crawler.en_prothomalo import get_latest_news
from crawler.en_prothomalo import formatter
import re

if __name__ == '__main__':
	news_text = "While in France, Jhon Reese discussed 100% short-term stimulus efforts in a recent interview with the Wall Street Journal."
	tagger = Tagger(stanford_classifier, stanford_ner_path)
	print tagger.entity_group(news_text)
