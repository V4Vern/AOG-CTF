#!/usr/bin/env python3
# Script to generate sqlite db file
import sqlite3

movieslist = [("Extraction","A black-market mercenary who has nothing to lose is hired to rescue the kidnapped son of an imprisoned international crime lord. But in the murky underworld of weapons dealers and drug traffickers, an already deadly mission approaches the impossible."),
              ("Spenser Confidential","To unravel a twisted murder conspiracy, a former police detective returns to Boston's criminal underworld."),
              ("#Alive 2020", "The film revolves around a video game live streamer's struggle for survival as he is forced to stay alone at his apartment in Seoul during a zombie apocalypse."),
              ("lucifer","Lucifer, a demon, returns from hell to reside in Los Angeles and runs a club. He soon gets involved with the local police and assists them in solving tricky criminal cases."),
              ("Shadowhunter","On her birthday, Clary Fray discovers a surprise concerning her life. The teenager is not who she thinks she is -- she comes from a long line of human-angel hybrids, called Shadowhunters, who hunt demons"),
              ("Hobbs and Shaw","Luke Hobbs and Deckard Shaw set aside their differences and partner up to protect the world from Brixton, a genetically enhanced super-soldier."),
              ("Mulan","To save her ailing father from serving in the Imperial Army, a fearless young woman disguises herself as a man to battle northern invaders in China."),
              ("Congrats","Near"),
              ("19CTF{pr3p4r3_70_u53_pr3p4r3d_57473m3n75}","wow u found me")]

conn = sqlite3.connect('../service/src/movies.db')
c = conn.cursor()
c.execute("CREATE TABLE movies (movietitle text, review text)")
c.executemany('INSERT INTO movies VALUES (?,?)',movieslist)
conn.commit()
conn.close()