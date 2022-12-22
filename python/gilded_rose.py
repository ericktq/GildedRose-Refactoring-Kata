# -*- coding: utf-8 -*-
Action_2="Sulfuras, Hand of Ragnaros"
class GildedRose(object):

    def __init__(self, items):
       self.items = items

    def update_quality(self):
        for item in self.items:
            if item.name=="Aged Brie":
                self.aged_brie(item)
            elif item.name==Action_2:
                self.sulfuras(item)
            elif item.name=="Backstage passes to a TAFKAL80ETC concert":
                self.backstage_passes(item)
            elif item.name=="Conjured Mana Cake":
                self.cake(item)
            else:
                self.vest_elixir(item)

            if item.quality<0:
                item.quality=0
            if item.quality>50 and  item.name!=Action_2:
                item.quality=50
            if item.name!=Action_2:
                item.sell_in-=1

    def sulfuras(self,item):
        self.sell_in=item.sell_in
        self.quality=item.quality

    def aged_brie(self,item):
        if item.sell_in>0:
            item.quality +=1
        else:
            item.quality +=2

    def backstage_passes(self,item):
        if item.sell_in >0:
            item.quality +=1
        if item.sell_in<=10:
            item.quality +=2
        elif item.sell_in<=5:
            item.quality +=3
        else:
             item.quality=0
    
    def cake(self,item):
        item.quality -=2
        if item.sell_in==0:
            item.quality=0
            


    def vest_elixir(self,item):
        if item.sell_in>0:
            item.quality -=1
        else:
            item.quality -=2
        if item.sell_in==0:
            item.quality=0
        



class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
