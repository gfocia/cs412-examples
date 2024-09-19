from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
import time
import random


# list of quotes 
quotes = [
    "No matter what happens in life, be good to people. Being good to people is a wonderful legacy to leave behind.", 
    "You have people come into your life shockingly and surprisingly. You have losses that you never thought you'd experience. You have rejection and you have learn how to deal with that and how to get up the next day and go on with it.", 
    "Silence speaks so much louder than screaming tantrums. Never give anyone an excuse to say that you're crazy.",
    "Childless Cat Lady", 
    "Anything you put your mind to and add your imagination into can make your life a lot better and a lot more fun.", 
    "At some point, you grow out of being attracted to that flame that burns you over and over and over again.", 
    "Red is such an interesting color to correlate with emotion, because it's on both ends of the spectrum. On one end you have happiness, falling in love, infatuation with someone, passion, all that. On the other end, you've got obsession, jealousy, danger, fear, anger and frustration.", 
    "Relationships are like traffic lights. And I just have this theory that I can only exist in a relationship if it's a green light.", 
    "Your feelings so are important to write down, to capture, and to remember because today you're heartbroken, but tomorrow you'll be in love again.", 
    "I second-guess and overthink and rethink every single thing that I do.", 
    "I've always felt music is the only way to give an instantaneous moment the feel of slow motion. To romanticise it and glorify it and give it a soundtrack and a rhythm.", 
    "When you are missing someone, time seems to move slower, and when I'm falling in love with someone, time seems to be moving faster.", 
    "I've never thought about songwriting as a weapon. I've only thought about it as a way to help me get through love and loss and sadness and loneliness and growing up.", 
    "I think that as you grow up, as you get older, we can't get bitter, we can't get jaded.", 
    "I have a terrifying long list of fears. Literally everything - diseases, spiders... and people getting tired of me.", 
    "I know my flaws before other people point them out to me.", 
    "I can't deal with someone wanting to take a relationship backward or needing space or cheating on you. It's a conscious thing; it's a common-sense thing.", 
    "Even if you're happy with the life you've chosen, you're still curious about the other options.", 
]
# list of image URLs 
images = [ 
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTsJVFD2EuKAYCvAzuLoQnxU6VtIyeqt8Wvzg&s", 
    "https://variety.com/wp-content/uploads/2024/02/Screen-Shot-2024-02-28-at-12.40.18-PM.png?w=1000&h=667&crop=1", 
    "https://cyberscoop.com/wp-content/uploads/sites/3/2024/09/GettyImages-2166943469.jpg?w=1024", 
    "https://variety.com/wp-content/uploads/2022/11/Taylor-Swift.jpg?w=1000&h=667&crop=1", 
    "https://pyxis.nymag.com/v1/imgs/360/29f/b2623a786d03de40f7effeb8b8dd207ec2-taylorswift.1x.rsquare.w1400.jpg", 
    "https://hls.harvard.edu/wp-content/uploads/2024/04/Taylor-Swift-concert-yellow-dress-GettyImages-2015112497-2400x1600-1.jpg", 
    "https://www.usatoday.com/gcdn/authoring/authoring-images/2024/09/11/PNAS/75183972007-2171410865.jpg?crop=2665,1499,x0,y200&width=660&height=371&format=pjpg&auto=webp", 
    "https://deadline.com/wp-content/uploads/2024/08/GettyImages-2158900890-e1723562761225.jpg?w=681&h=383&crop=1", 
    "https://cdn.britannica.com/85/182085-050-EB0D9C57/Taylor-Swift-2013.jpg", 
    "https://www.billboard.com/wp-content/uploads/2024/06/taylor-swift-eras-tour-liverpool-tortured-poets-june-2023-billboard-1548.jpg?w=942&h=623&crop=1", 
    "https://media-cldnry.s-nbcnews.com/image/upload/t_fit-1240w,f_auto,q_auto:best/rockcms/2023-05/taylor-swift-speak-now-purple-today-sk-230505-c46151.jpg", 
    "https://img-cdn.inc.com/image/upload/w_600,ar_16:9,c_fill,g_auto,q_auto:best/images/panoramic/taylor-swift-emotional-intelligence_535637_cwnhmj.webp", 
    "https://madmuseum.org/sites/default/files/styles/page_hero/public/2023/04/IBYTAM_still-page.jpg?itok=cVPWukbf", 
    "https://e3.365dm.com/23/08/2048x1152/skynews-taylor-swift-santa-clara_6237922.jpg", 
    "https://www.rollingstone.com/wp-content/uploads/2024/07/GettyImages-2160782996.jpg?w=1581&h=1054&crop=1", 
    "https://media.cnn.com/api/v1/images/stellar/prod/20240819-donald-trump-taylor-swift-split.jpg?c=16x9&q=h_833,w_1480,c_fill", 
    "https://assets.teenvogue.com/photos/641b2a23912ddccbabf80f80/16:9/w_2560%2Cc_limit/GettyImages-1474459622.jpg", 
    "https://i8.amplience.net/i/naras/taylor-swift_MI0005380911-MN0000472102", 
    "https://www.billboard.com/wp-content/uploads/2024/08/taylor-swift-eras-tour-london-reputation-aug-2024-billboard-1548.jpg?w=942&h=623&crop=1", 
    "https://media.cnn.com/api/v1/images/stellar/prod/gettyimages-2160776847.jpg?c=16x9&q=h_833,w_1480,c_fill", 
]

# this view directs the application to display one quote and one image 
def quote(request): 

    template_name = "quotes/quote.html"

    one_random_quote = random.choice(quotes)
    one_random_image = random.choice(images)

    context = {
        'quote': one_random_quote,
        'image': one_random_image,
    }
    return render(request, template_name, context)


# this view will add the entire list of quotes and images to the context data for the view. 
def show_all(request): 

    template_name = "quotes/show_all.html"
    zipped_data = zip(quotes, images)
    context = {
        'zipped_data': zipped_data
    }
    return render(request, template_name, context)


# this view will display information about the famous person whose quotes are shown in this application.
def about(request): 

    template_name = "quotes/about.html"

    context = {
        'biography': "Taylor Swift (born December 13, 1989, West Reading, Pennsylvania, U.S.) is a multitalented singer-songwriter and global superstar who has captivated audiences with her heartfelt lyrics and catchy melodies, solidifying herself as one of the most influential artists in contemporary music. In 2024 she made history when she won the Grammy Award for album of the year for Midnights (2022), becoming the first artist to win in that category four times.Swift showed an interest in music at an early age, and she progressed quickly from roles in children's theater to her first appearance before a crowd of thousands. She was age 11 when she sang “The Star-Spangled Banner” before a Philadelphia 76ers basketball game, and the following year she picked up the guitar and began to write songs. Taking her inspiration from country music artists such as Shania Twain and the Dixie Chicks (now the Chicks), Swift crafted original material that reflected her experiences of tween alienation. When she was 13, Swift's parents sold their farm in Pennsylvania to move to Hendersonville, Tennessee, so she could devote more of her time to courting country labels in nearby Nashville. A development deal with RCA Records allowed Swift to make the acquaintance of recording-industry veterans, and in 2004, at age 14, she signed with Sony/ATV as a songwriter. At venues in the Nashville area, she performed many of the songs she had written, and it was at one such performance that she was noticed by record executive Scott Borchetta. Borchetta signed Swift to his fledgling Big Machine label, and her first single, “Tim McGraw” (inspired by and prominently referencing a song by Swift's favorite country artist), was released in the summer of 2006. The song was an immediate success, spending eight months on the Billboard country singles chart. Now age 16, Swift followed with a self-titled debut album, and she went on tour, opening for Rascal Flatts. Taylor Swift was certified platinum in 2007, having sold more than one million copies in the United States, and Swift continued a rigorous touring schedule, opening for artists such as George Strait, Kenny Chesney, Tim McGraw, and Faith Hill. That November Swift received the Horizon Award for best new artist from the Country Music Association (CMA), capping the year in which she emerged as country music's most-visible young star. On Swift's second album, Fearless (2008), she demonstrated a refined pop sensibility, managing to court the mainstream pop audience without losing sight of her country roots. With sales of more than half a million copies in its first week, Fearless opened at number one on the Billboard 200 chart. It ultimately spent more time atop that chart than any other album released that decade. Singles such as “You Belong with Me” and “Love Story” were popular in the digital market as well, the latter accounting for more than four million paid downloads. In 2009 Swift embarked on her first tour as a headliner, playing to sold-out venues across North America. That year also saw Swift dominate the industry award circuit. Fearless was recognized as album of the year by the Academy of Country Music in April, and she topped the best female video category for “You Belong with Me” at the MTV Video Music Awards (VMAs) in September. During her VMA acceptance speech, Swift was interrupted by rapper Kanye West, who protested that the award should have gone to Beyoncé for what he called “one of the best videos of all time.” Later in the program, when Beyoncé was accepting the award for video of the year, she invited Swift onstage to conclude her speech, a move that drew a standing ovation for both performers. At the CMA Awards that November, Swift won all four categories in which she was nominated. Her recognition as CMA entertainer of the year made her the youngest-ever winner of that award, as well as the first female solo artist to win since 1999. She began 2010 with an impressive showing at the Grammy Awards, where she collected four honors, including best country song, best country album, and the top prize of album of the year. Later that year Swift made her feature-film debut in the romantic comedy Valentine's Day and was named the new spokesperson for CoverGirl cosmetics. Although Swift avoided discussing her personal life in interviews, she was surprisingly frank in her music. Her third album, Speak Now (2010), was littered with allusions to romantic relationships with John Mayer, Joe Jonas of the Jonas Brothers, and Twilight series actor Taylor Lautner. Swift reclaimed the CMA entertainer of the year award in 2011, and the following year she won Grammys for best country solo performance and best country song for “Mean,” a single from Speak Now. Swift continued her acting career with a voice role in the animated Dr. Seuss' The Lorax (2012) before releasing her next collection of songs, Red (2012). While she remained focused on the vagaries of young love, her songwriting reflected a deepened perspective on the subject, and much of the album embraced a bold pop-rock sound. In its first week on sale in the United States, Red sold 1.2 million copies—the highest one-week total in 10 years. In addition, its lead single, the gleeful “We Are Never Ever Getting Back Together,” gave Swift her first number-one hit on the Billboard pop singles chart. In 2014 Swift released 1989, an album titled after the year of her birth and reportedly inspired by the music of that era. Although Swift had already been steadily moving away from the traditional country signifiers that marked her early work—“I Knew You Were Trouble,” the second single from Red, even flirted with electronic dance music—she called 1989 her first “official pop album.” On the strength of the upbeat “Shake It Off,” the album proved to be another blockbuster for Swift, its first-week sales surpassing those of Red. It went on to sell more than five million copies in the United States and earned Swift her second Grammy for album of the year. In 2014 Swift also appeared in a supporting role in The Giver, a film adaptation of Lois Lowry's dystopian novel for young readers. In 2016 Swift's feud with Kanye West resumed after he released the single “Famous.” The song included a lyric in which Swift was referred to as a “bitch,” and she alleged that it was misogynistic. The public spat escalated after West's wife, Kim Kardashian, released a recording of a phone call in which Swift gave her approval for the line, though West made no mention of calling her a bitch. Swift's controversies continued as she took part in a widely publicized civil trial in August 2017, after former radio host David Mueller sued the singer, her mother, and a promoter, claiming that Swift had falsely accused him of sexually groping her in 2013 during the taking of a photograph and thus destroyed his career. She countersued, maintaining that the assault had taken place. At the trial, Swift was removed from Mueller's suit and the other two defendants were found not liable as the jury found in favor of Swift's countersuit. Shortly thereafter Swift released the hit song “Look What You Made Me Do,” and her album Reputation became the top-selling American LP of 2017. In 2018 Swift left Big Machine and signed with Republic Records and Universal Music Group. The following year her former label, which owned the master recordings of her six albums, was sold to Scooter Braun, a talent manager whose clients had included Kanye West. Swift publicly spoke out against the deal, claiming that Borchetta had rejected her attempts to acquire the master tapes and that Braun had bullied her over the years. She subsequently tried to negotiate a deal with Braun, but he sold her back catalog to a private investment firm in 2020. Against this backdrop, Swift began rerecording her early material in an effort to gain control of it—the hope being that her remade songs and not the originals would be sought out for licensing deals—and in 2021 Fearless (Taylor's Version) and Red (Taylor's Version) appeared. They were remakes of earlier albums with several previously unreleased tracks. In July 2023 Swift released Speak Now (Taylor's Version), followed by 1989 (Taylor's Version) in October that same year. In 2019 Swift released her seventh album, Lover, which she described as “a love letter to love itself.” That year she also appeared in the musical Cats, a film adaptation of Andrew Lloyd Webber's hugely successful stage production. Miss Americana (2020) is a documentary about her life and career. With little advance notice, she released Folklore in 2020. A departure from her previous pop-inspired work, Swift's eighth studio album drew praise for its introspection and restraint, and it won the Grammy for album of the year. The “sister record,” Evermore, appeared later in 2020. Swift adopted a synth-pop sound for the candid Midnights (2022), which she described as “the story of 13 sleepless nights scattered throughout my life.” The album received six Grammy nominations, scoring wins for album of the year and best pop vocal album. March 2023 marked the start of Swift's first concert tour since 2018, her sixth tour overall. When ticket sales for the Eras Tour opened on Ticketmaster in November 2022, many fans were disappointed by technical issues and waits that lasted up to multiple days. After two rounds of presales, general sales were canceled due to unprecedented demand. Swift expressed disappointment about the situation but did not mention Ticketmaster in her response. In December 2023, Swift was honored as Time magazine's “Person of the Year.” Finalists also included Barbie, Vladimir Putin, and Sam Altman. The honor came shortly after the music streaming platform Spotify deemed her its most-played artist. According to a Bloomberg analysis, Swift is now a billionaire, with a net worth of around $1.1 billion. On a Forbes list of the most powerful women of 2023, Swift placed fifth. She has been dating American football player Travis Kelce since October 2023. In February 2024, while accepting one of her awards during the Grammy Awards telecast, Swift announced that she would be releasing her next studio album, The Tortured Poets Department, in April. The album was released as a double LP, the 15-track second part dubbed The Tortured Poets Department: The Anthology. Guest artists include Post Malone on the single “Fortnight” and Florence Welch on the track “Florida!!!”. At the 2024 MTV Video Music Awards (VMAs), Swift received seven awards, bringing her total count up to 30 and tying her with Beyoncé for solo artist with the most VMAs won during their career. She also left the awards with the most VMAs for Best Director (for “Fortnight”). She had previously been tied with three VMAs with directors David Fincher and Spike Jonze.",
        'creator': "Created by Georgina Focia.",
    }
    return render(request, template_name, context)

