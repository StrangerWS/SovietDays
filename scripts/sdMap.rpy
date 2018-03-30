init -1001 python:
    def sdDisableAllChibi():
        global sdGlobalZones
        for name, data in sdGlobalZones.iteritems():
            data["map_chibi"] = None
            
init -997 python:
    store.sdMapPics = {
        "sdBgMap": sdGetImage("gui/map/map_bg.jpg"),
        "sdAvaliableMap": sdGetImage("gui/map/map_avaliable.jpg"),
        "sdSelectedMap": sdGetImage("gui/map/map_selected.jpg")
    }
    store.map_chibi = {
        "?" : sdGetImage("gui/map/map_icon_n00.png"),
        "me": sdGetImage("gui/map/map_icon_n01.png"),
        "mi": sdGetImage("gui/map/map_icon_n02.png"),
        "sh": sdGetImage("gui/map/map_icon_n03.png"),
        "el": sdGetImage("gui/map/map_icon_n04.png"),
        "mz": sdGetImage("gui/map/map_icon_n05.png"),
        "mt": sdGetImage("gui/map/map_icon_n06.png"),
        "uv": sdGetImage("gui/map/map_icon_n07.png"),
        "un": sdGetImage("gui/map/map_icon_n08.png"),
        "us": sdGetImage("gui/map/map_icon_n09.png"),
        "dv": sdGetImage("gui/map/map_icon_n10.png"),
        "sl": sdGetImage("gui/map/map_icon_n11.png"),
        "cs": sdGetImage("gui/map/map_icon_n12.png"),
    }

init -996 python:
    store.sdMapZones = {
            "sd_sl_mt_house":   {"position":[960,178,992,227],"default_bg":bg_tmp_image(u"Славя и вожатая")},
            "sd_estrade":       {"position":[1062,54,1154,135],"default_bg":bg_tmp_image(u"Эстрада")},
            "sd_music_club":    {"position":[627,255,692,337],"default_bg":bg_tmp_image(u"Музклуб")},
            "sd_square":        {"position":[887,360,998,545],"default_bg":bg_tmp_image(u"Площадь")},
            "sd_dining_hall":   {"position":[1010,458,1137,606],"default_bg":bg_tmp_image(u"Столовая")},
            "sd_sport_area":    {"position":[1220,481,1574,658],"default_bg":bg_tmp_image(u"Спорткомплекс")},
            "sd_beach":         {"position":[1198,674,1488,831],"default_bg":bg_tmp_image(u"Пляж")},
            "sd_boat_station":  {"position":[832,801,957,855],"default_bg":bg_tmp_image(u"Лодочный причал")},
            "sd_clubs":         {"position":[437,437,657,607],"default_bg":bg_tmp_image(u"Клубы")},
            "sd_library":       {"position":[1158,271,1285,357],"default_bg":bg_tmp_image(u"Библиотека")},
            "sd_medic_house":   {"position":[1042,357,1138,444],"default_bg":bg_tmp_image(u"Медпункт")},
            "sd_camp_entrance": {"position":[284,440,412,554],"default_bg":bg_tmp_image(u"Ворота в лагерь")},
            "sd_forest":        {"position":[562,50,690,188],"default_bg":bg_tmp_image(u"о. Лес")},
            "sd_un_mi_house":   {"position":[811,154,848,195],"default_bg":bg_tmp_image(u"Лена и Мику")},
            "sd_me_mz_house":   {"position":[1027,257,1058,300],"default_bg":bg_tmp_image(u"Мой домик")},
            "sd_el_sh_house":   {"position":[854,292,884,331],"default_bg":bg_tmp_image(u"Эл и Шурик")},
            "sd_dv_us_house":   {"position":[717,624,758,670],"default_bg":bg_tmp_image(u"Алиса и Ульяна")},
            "sd_shed":          {"position":[1144,488,1211,584],"default_bg":bg_tmp_image(u"Склад")},
            "sd_admin_house":   {"position":[790,350,860,447],"default_bg":bg_tmp_image(u"Администрация")},
            "sd_old_house":     {"position":[238,1005,340,1071],"default_bg":bg_tmp_image(u"Старый корпус")}

    }


init -51 python:
    sdGlobalMapResult = "error"
    def sdInitMapZonesRealization(sdZones, default):
        global sdGlobalZones
        sdGlobalZones = sdZones
        for i, data in sdGlobalZones.iteritems():
            data["chibi"] = None
            data["avaliable"] = True
            data["label"] = default
            data["been_here"] = 0
            
    class sdMap(renpy.Displayable):
        def __init__(self,pics,chibi,default):
            renpy.Displayable.__init__(self)
            self.pics=pics
            self.chibi=chibi
            self.default=default
            config.overlay_functions.append(self.overlay)

        def disable_all_zones(self):
            global sdGlobalZones
            for name,data in sdGlobalZones.iteritems():
                data["label"] = self.default
                data["avaliable"] = False
                data["been_here"] = 0
        def enable_all_zones(self):
            global sdGlobalZones
            for name,data in sdGlobalZones.iteritems():
                data["label"] = self.default
                data["avaliable"] = True
                data["been_here"] = 0
        def set_zone(self,name,label):
            global sdGlobalZones
            sdGlobalZones[name]["label"] = label
            sdGlobalZones[name]["avaliable"] = True
        def reset_zone(self,name):
            global sdGlobalZones
            sdGlobalZones[name]["label"] = self.default
            sdGlobalZones[name]["avaliable"] = False
            sdGlobalZones[name]["been_here"] = 0
        def enable_empty_zone(self,name):
            global sdGlobalZones
            self.set_zone(name,self.default)
            sdGlobalZones[name]["avaliable"] = True
        def reset_current_zone(self):
            self.enable_empty_zone(sdGlobalMapResult)
        def disable_current_zone(self):
            global sdGlobalZones
            sdGlobalZones[sdGlobalMapResult]["avaliable"] = False
        def been_there(self):
            global sdGlobalZones
            return sdGlobalZones[sdGlobalMapResult]["been_here"]
        def set_chibi(self,name,ch):
            global sdGlobalZones
            if  ch in self.chibi:
                sdGlobalZones[name]["chibi"] = self.chibi[ch]
            else:
                sdGlobalZones[name]["chibi"] = None
        def reset_chibi(self,name):
            self.set_chibi(name,"")
        def event(self, ev, x, y, st):
            return
        def render(self, width, height, st, at):
            return renpy.Render(1, 1)
        def zoneclick(self,name):
            global sdGlobalZones
            global sdGlobalMapResult
            store.sdMapEnabled=False
            renpy.scene('mapoverlay')
            sdGlobalZones[name]["been_here"] += 1
            sdGlobalMapResult = name
            renpy.scene()
            #if not not_in_rollback_or_fast_forward():
            #   renpy.log("renpy.roll_forward_info()")
            #    renpy.config.skipping = False
            #    renpy.game.after_rollback = False
            ui.jumps(sdGlobalZones[name]["label"])()
        def overlay(self):
            if  store.sdMapEnabled:
                global sdGlobalZones
                renpy.scene('mapoverlay')
                ui.layer('mapoverlay')
                for name,data in sdGlobalZones.iteritems():
                    if data["avaliable"]:
                        pos = data["position"]
                        ui.imagebutton(
                            im.Crop(self.pics["sdAvaliableMap"],pos[0],pos[1],pos[2]-pos[0],pos[3]-pos[1]),
                            im.Crop(self.pics["sdSelectedMap"], pos[0],pos[1],pos[2]-pos[0],pos[3]-pos[1]),
                            clicked = renpy.curry(self.zoneclick)(name),
                            xpos = pos[0],
                            ypos = pos[1]
                        )
                        if  data["chibi"] != None:
                            ui.imagebutton(
                                anim.Blink(data["chibi"]),
                                anim.Blink(data["chibi"]),
                                clicked = renpy.curry(self.zoneclick)(name),
                                xpos = pos[0],
                                ypos = pos[1]
                            )
                ui.close()
                
    store.sdWorkMap = sdMap(store.sdMapPics, store.map_chibi, default)
        
    import pygame
    import os
    import os.path
    from renpy.store import *
    from renpy.display.im import ImageBase, image, cache, Composite

    store.sdMapEnabled = False
    store.sdMapEnabledTmp = False
    def disable_stuff():
        store.sdMapEnabledTmp = store.sdMapEnabledTmp or store.sdMapEnabled
        store.sdMapEnabled = False
    def enable_stuff():
        store.sdMapEnabled = store.sdMapEnabledTmp
        store.sdMapEnabledTmp = False
        
init 5 python:
    import renpy.store as store 
    if True:
        def sdDisableAllZones():
            store.sdWorkMap.disable_all_zones()
        def sdEnableAllZones():
            store.sdWorkMap.enable_all_zones()
        def sdSetZone(name,label):
            store.sdWorkMap.set_zone(name,label)
        def sdResetZone(name):
            store.sdWorkMap.reset_zone(name)
        def sdEnableEmptyZone(name):
            store.sdWorkMap.enable_empty_zone(name)
        def sdResetCurrentZone():
            store.sdWorkMap.reset_current_zone()
        def sdDisableCurrentZone():
            store.sdWorkMap.disable_current_zone()
        def sdBeenThere():
            return store.sdWorkMap.been_there()
        def sdSetChibi(name,ch):
            store.sdWorkMap.set_chibi(name,ch)
        def sdResetChibi(name):
            store.sdWorkMap.reset_chibi(name)
        def sdShowMap():
            ui.jumps("sdShow")()
        def sdInitMapZones():
            sdInitMapZonesRealization(store.sdMapZones,"nothing_here")
            
init 5:
    if True:
        image widget sdWorkMap = sdGetImage("gui/map/map_bg.jpg")
        image bg sdWorkMap = sdGetImage("gui/map/map_bg.jpg")

init 52 python:
    def sdDisableAllChibi():
        global sdGlobalZones
        for name,data in sdGlobalZones.iteritems():
            data["chibi"] = None    

label sdShow:
    scene widget sdWorkMap
    $ store.sdMapEnabled = True
    $ ui.interact()
    jump sdShow
