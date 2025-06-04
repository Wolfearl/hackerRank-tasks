#!/bin/python3

import math
import os
import random
import re
import sys


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.prefix_found = False

    def insert(self, word):
        if self.prefix_found:
            return
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            if node.is_end_of_word:
                self.prefix_found = True
                print("BAD SET")
                print(word)
                return
        if len(node.children) > 0:
            self.prefix_found = True
            print("BAD SET")
            print(word)
            return
        node.is_end_of_word = True


def noPrefix(words):
    trie = Trie()
    for word in words:
        trie.insert(word)
    if not trie.prefix_found:
        print("GOOD SET")


if __name__ == '__main__':
    n = 100

    # words = ['aab', 'defgab', 'abcde', 'aabcde', 'bbbbbbbbbb', 'jabjjjad']

    words = []
    s = '''hihihihih
hihihih'''
#     s = '''hgiiccfchbeadgebc
# biiga
# edchgb
# ccfdbeajaeid
# ijgbeecjbj
# bcfbbacfbfcfbhcbfjafibfhffac
# ebechbfhfcijcjbcehbgbdgbh
# ijbfifdbfifaidje
# acgffegiihcddcdfjhhgadfjb
# ggbdfdhaffhghbdh
# dcjaichjejgheiaie
# d
# jeedfch
# ahabicdffbedcbdeceed
# fehgdfhdiffhegafaaaiijceijdgbb
# beieebbjdgdhfjhj
# ehg
# fdhiibhcbecddgijdb
# jgcgafgjjbg
# c
# fiedahb
# bhfhjgcdbjdcjjhaebejaecdheh
# gbfbbhdaecdjaebadcggbhbchfjg
# jdjejjg
# dbeedfdjaghbhgdhcedcj
# decjacchhaciafafdgha
# a
# hcfibighgfggefghjh
# ccgcgjgaghj
# bfhjgehecgjchcgj
# bjbhcjcbbhf
# daheaggjgfdcjehidfaedjfccdafg
# efejicdecgfieef
# ciidfbibegfca
# jfhcdhbagchjdadcfahdii
# i
# abjfjgaghbc
# bddeejeeedjdcfcjcieceieaei
# cijdgbddbceheaeececeeiebafgi
# haejgebjfcfgjfifhihdbddbacefd
# bhhjbhchdiffb
# jbbdhcbgdefifhafhf
# ajhdeahcjjfie
# idjajdjaebfhhaacecb
# bhiehhcggjai
# bjjfjhiice
# aif
# gbbfjedbhhhjfegeeieig
# fefdhdaiadefifjhedaieaefc
# hgaejbhdebaacbgbgfbbcad
# heghcb
# eggadagajjgjgaihjdigihfhfbijbh
# jadeehcciedcbjhdeca
# ghgbhhjjgghgie
# ibhihfaeeihdffjgddcj
# hiedaegjcdai
# bjcdcafgfjdejgiafdhfed
# fgdgjaihdjaeefejbbijdbfabeie
# aeefgiehgjbfgidcedjhfdaaeigj
# bhbiaeihhdafgaciecb
# igicjdajjdegbceibgebedghihihh
# baeeeehcbffd
# ajfbfhhecgaghgfdadbfbb
# ahgaccehbgajcdfjihicihhc
# bbjhih
# a
# cdfcdejacaicgibghgddd
# afeffehfcfiefhcagg
# ajhebffeh
# e
# hhahehjfgcj
# ageaccdcbbcfidjfc
# gfcjahbbhcbggadcaebae
# gi
# edheggceegiedghhdfgabgcd
# hejdjjbfacggdccgahiai
# ffgeiadgjfgecdbaebagij
# dgaiahge
# hdbaifh
# gbhccajcdebcig
# ejdcbbeiiebjcagfhjfdahbif
# g
# ededbjaaigdhb
# ahhhcibdjhidbgefggdjebfcf
# bdigjaehfchebiedajcjdh
# fjehjgbdbaiifi
# fbgigbdcbcgffdicfcidfdafghajc
# ccajeeijhhb
# gaaagfacgiddfahejhbgdfcfbfeedh
# gdajaigfbjcdegeidgaccjfi
# fghechfchjbaebcghfcfbdicgaic
# cfhigaciaehacdjhfcgajgbhhgj
# edhjdbdjccbfihiaddij
# cbbhagjbcadegicgifgghai
# hgdcdhieji
# fbifgbhdhagch
# cbgcdjea
# dggjafcajhbbbaja
# bejihed
# eeahhcggaaidifdigcfjbficcfhjj'''

    words = list(s.split("\n"))
    # for _ in range(n):
    #     words_item = input()
    #     words.append(words_item)

    noPrefix(words)
