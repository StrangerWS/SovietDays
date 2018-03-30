init -1001:
    image mz cry pioneer = ConditionSwitch(
            "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "images/sprites/normal/mz/mz_1_body.png", (0, 0), "images/sprites/normal/mz/mz_1_pioneer.png", (0, 0), "SovietDays/res/image/sprites/normal/mz/mz_1_cry.png"), im.matrix.tint(0.94, 0.82, 1.0)),
            "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "images/sprites/normal/mz/mz_1_body.png", (0, 0), "images/sprites/normal/mz/mz_1_pioneer.png", (0, 0), "SovietDays/res/image/sprites/normal/mz/mz_1_cry.png"), im.matrix.tint(0.63, 0.78, 0.82)),
            True, im.Composite((900, 1080), (0, 0), "images/sprites/normal/mz/mz_1_body.png", (0, 0), "images/sprites/normal/mz/mz_1_pioneer.png", (0, 0), "SovietDays/res/image/sprites/normal/mz/mz_1_cry.png"))
        
    image mz cry glasses pioneer = ConditionSwitch(
            "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "images/sprites/normal/mz/mz_1_body.png", (0, 0), "images/sprites/normal/mz/mz_1_pioneer.png", (0, 0), "SovietDays/res/image/sprites/normal/mz/mz_1_cry.png", (0, 0), "images/sprites/normal/mz/mz_1_glasses.png"), im.matrix.tint(0.94, 0.82, 1.0)),
            "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "images/sprites/normal/mz/mz_1_body.png", (0, 0), "images/sprites/normal/mz/mz_1_pioneer.png", (0, 0), "SovietDays/res/image/sprites/normal/mz/mz_1_cry.png", (0, 0), "images/sprites/normal/mz/mz_1_glasses.png"), im.matrix.tint(0.63, 0.78, 0.82)),
            True, im.Composite((900, 1080), (0, 0), "images/sprites/normal/mz/mz_1_body.png", (0, 0), "images/sprites/normal/mz/mz_1_pioneer.png", (0, 0), "SovietDays/res/image/sprites/normal/mz/mz_1_cry.png", (0, 0), "images/sprites/normal/mz/mz_1_glasses.png"))

    image us grin pioneer bear = ConditionSwitch(
            "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "images/sprites/normal/us/us_1_body.png", (0, 0), "images/sprites/normal/us/us_1_pioneer.png", (0, 0), "SovietDays/res/image/sprites/normal/us/us_1_bear.png", (0, 0), "images/sprites/normal/us/us_1_grin.png"), im.matrix.tint(0.94, 0.82, 1.0)),
            "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "images/sprites/normal/us/us_1_body.png", (0, 0), "images/sprites/normal/us/us_1_pioneer.png", (0, 0), "SovietDays/res/image/sprites/normal/us/us_1_bear.png", (0, 0), "images/sprites/normal/us/us_1_grin.png"), im.matrix.tint(0.63, 0.78, 0.82)),
            True, im.Composite((900, 1080), (0, 0), "images/sprites/normal/us/us_1_body.png", (0, 0), "images/sprites/normal/us/us_1_pioneer.png", (0, 0), "SovietDays/res/image/sprites/normal/us/us_1_bear.png", (0, 0), "images/sprites/normal/us/us_1_grin.png"))
            
    image us laugh pioneer bear = ConditionSwitch(          
            "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "images/sprites/normal/us/us_1_body.png", (0, 0), "images/sprites/normal/us/us_1_pioneer.png", (0, 0), "SovietDays/res/image/sprites/normal/us/us_1_bear.png", (0, 0), "images/sprites/normal/us/us_1_laugh.png"), im.matrix.tint(0.94, 0.82, 1.0)),
            "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "images/sprites/normal/us/us_1_body.png", (0, 0), "images/sprites/normal/us/us_1_pioneer.png", (0, 0), "SovietDays/res/image/sprites/normal/us/us_1_bear.png", (0, 0), "images/sprites/normal/us/us_1_laugh.png"), im.matrix.tint(0.63, 0.78, 0.82)),
            True, im.Composite((900, 1080), (0, 0), "images/sprites/normal/us/us_1_body.png", (0, 0), "images/sprites/normal/us/us_1_pioneer.png", (0, 0), "SovietDays/res/image/sprites/normal/us/us_1_bear.png", (0, 0), "images/sprites/normal/us/us_1_laugh.png"))
    
    image us laugh2 pioneer bear = ConditionSwitch(
            "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "images/sprites/normal/us/us_1_body.png", (0, 0), "images/sprites/normal/us/us_1_pioneer.png", (0, 0), "SovietDays/res/image/sprites/normal/us/us_1_bear.png", (0, 0), "images/sprites/normal/us/us_1_laugh2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
            "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "images/sprites/normal/us/us_1_body.png", (0, 0), "images/sprites/normal/us/us_1_pioneer.png", (0, 0), "SovietDays/res/image/sprites/normal/us/us_1_bear.png", (0, 0), "images/sprites/normal/us/us_1_laugh2.png"), im.matrix.tint(0.63, 0.78, 0.82)),
            True, im.Composite((900, 1080), (0, 0), "images/sprites/normal/us/us_1_body.png", (0, 0), "images/sprites/normal/us/us_1_pioneer.png", (0, 0), "SovietDays/res/image/sprites/normal/us/us_1_bear.png", (0, 0), "images/sprites/normal/us/us_1_laugh2.png"))
    
    image us normal pioneer bear = ConditionSwitch(
            "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "images/sprites/normal/us/us_1_body.png", (0, 0), "images/sprites/normal/us/us_1_pioneer.png", (0, 0), "SovietDays/res/image/sprites/normal/us/us_1_bear.png", (0, 0), "images/sprites/normal/us/us_1_normal.png"), im.matrix.tint(0.94, 0.82, 1.0)),
            "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "images/sprites/normal/us/us_1_body.png", (0, 0), "images/sprites/normal/us/us_1_pioneer.png", (0, 0), "SovietDays/res/image/sprites/normal/us/us_1_bear.png", (0, 0), "images/sprites/normal/us/us_1_normal.png"), im.matrix.tint(0.63, 0.78, 0.82)),
            True, im.Composite((900, 1080), (0, 0), "images/sprites/normal/us/us_1_body.png", (0, 0), "images/sprites/normal/us/us_1_pioneer.png", (0, 0), "SovietDays/res/image/sprites/normal/us/us_1_bear.png", (0, 0), "images/sprites/normal/us/us_1_normal.png"))
    
    image us sad pioneer bear = ConditionSwitch(
            "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "images/sprites/normal/us/us_1_body.png", (0, 0), "images/sprites/normal/us/us_1_pioneer.png", (0, 0), "SovietDays/res/image/sprites/normal/us/us_1_bear.png", (0, 0), "images/sprites/normal/us/us_1_sad.png"), im.matrix.tint(0.94, 0.82, 1.0)),
            "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "images/sprites/normal/us/us_1_body.png", (0, 0), "images/sprites/normal/us/us_1_pioneer.png", (0, 0), "SovietDays/res/image/sprites/normal/us/us_1_bear.png", (0, 0), "images/sprites/normal/us/us_1_sad.png"), im.matrix.tint(0.63, 0.78, 0.82)),
            True, im.Composite((900, 1080), (0, 0), "images/sprites/normal/us/us_1_body.png", (0, 0), "images/sprites/normal/us/us_1_pioneer.png", (0, 0), "SovietDays/res/image/sprites/normal/us/us_1_bear.png", (0, 0), "images/sprites/normal/us/us_1_sad.png"))
    
    image us smile pioneer bear  = ConditionSwitch(
            "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "images/sprites/normal/us/us_1_body.png", (0, 0), "images/sprites/normal/us/us_1_pioneer.png", (0, 0), "SovietDays/res/image/sprites/normal/us/us_1_bear.png", (0, 0), "images/sprites/normal/us/us_1_smile.png"), im.matrix.tint(0.94, 0.82, 1.0)),
            "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "images/sprites/normal/us/us_1_body.png", (0, 0), "images/sprites/normal/us/us_1_pioneer.png", (0, 0), "SovietDays/res/image/sprites/normal/us/us_1_bear.png", (0, 0), "images/sprites/normal/us/us_1_smile.png"), im.matrix.tint(0.63, 0.78, 0.82)),
            True, im.Composite((900, 1080), (0, 0), "images/sprites/normal/us/us_1_body.png", (0, 0), "images/sprites/normal/us/us_1_pioneer.png", (0, 0), "SovietDays/res/image/sprites/normal/us/us_1_bear.png", (0, 0), "images/sprites/normal/us/us_1_smile.png"))
            
    image us grin sport bear = ConditionSwitch(
            "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "images/sprites/normal/us/us_1_body.png", (0, 0), "images/sprites/normal/us/us_1_sport.png", (0, 0), "SovietDays/res/image/sprites/normal/us/us_1_bear.png", (0, 0), "images/sprites/normal/us/us_1_grin.png"), im.matrix.tint(0.94, 0.82, 1.0)),
            "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "images/sprites/normal/us/us_1_body.png", (0, 0), "images/sprites/normal/us/us_1_sport.png", (0, 0), "SovietDays/res/image/sprites/normal/us/us_1_bear.png", (0, 0), "images/sprites/normal/us/us_1_grin.png"), im.matrix.tint(0.63, 0.78, 0.82)),
            True, im.Composite((900, 1080), (0, 0), "images/sprites/normal/us/us_1_body.png", (0, 0), "images/sprites/normal/us/us_1_sport.png", (0, 0), "SovietDays/res/image/sprites/normal/us/us_1_bear.png", (0, 0), "images/sprites/normal/us/us_1_grin.png"))
            
    image us laugh sport bear = ConditionSwitch(            
            "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "images/sprites/normal/us/us_1_body.png", (0, 0), "images/sprites/normal/us/us_1_sport.png", (0, 0), "SovietDays/res/image/sprites/normal/us/us_1_bear.png", (0, 0), "images/sprites/normal/us/us_1_laugh.png"), im.matrix.tint(0.94, 0.82, 1.0)),
            "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "images/sprites/normal/us/us_1_body.png", (0, 0), "images/sprites/normal/us/us_1_sport.png", (0, 0), "SovietDays/res/image/sprites/normal/us/us_1_bear.png", (0, 0), "images/sprites/normal/us/us_1_laugh.png"), im.matrix.tint(0.63, 0.78, 0.82)),
            True, im.Composite((900, 1080), (0, 0), "images/sprites/normal/us/us_1_body.png", (0, 0), "images/sprites/normal/us/us_1_sport.png", (0, 0), "SovietDays/res/image/sprites/normal/us/us_1_bear.png", (0, 0), "images/sprites/normal/us/us_1_laugh.png"))
    
    image us laugh2 sport bear = ConditionSwitch(
            "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "images/sprites/normal/us/us_1_body.png", (0, 0), "images/sprites/normal/us/us_1_sport.png", (0, 0), "SovietDays/res/image/sprites/normal/us/us_1_bear.png", (0, 0), "images/sprites/normal/us/us_1_laugh2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
            "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "images/sprites/normal/us/us_1_body.png", (0, 0), "images/sprites/normal/us/us_1_sport.png", (0, 0), "SovietDays/res/image/sprites/normal/us/us_1_bear.png", (0, 0), "images/sprites/normal/us/us_1_laugh2.png"), im.matrix.tint(0.63, 0.78, 0.82)),
            True, im.Composite((900, 1080), (0, 0), "images/sprites/normal/us/us_1_body.png", (0, 0), "images/sprites/normal/us/us_1_sport.png", (0, 0), "SovietDays/res/image/sprites/normal/us/us_1_bear.png", (0, 0), "images/sprites/normal/us/us_1_laugh2.png"))
    
    image us normal sport bear = ConditionSwitch(
            "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "images/sprites/normal/us/us_1_body.png", (0, 0), "images/sprites/normal/us/us_1_sport.png", (0, 0), "SovietDays/res/image/sprites/normal/us/us_1_bear.png", (0, 0), "images/sprites/normal/us/us_1_normal.png"), im.matrix.tint(0.94, 0.82, 1.0)),
            "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "images/sprites/normal/us/us_1_body.png", (0, 0), "images/sprites/normal/us/us_1_sport.png", (0, 0), "SovietDays/res/image/sprites/normal/us/us_1_bear.png", (0, 0), "images/sprites/normal/us/us_1_normal.png"), im.matrix.tint(0.63, 0.78, 0.82)),
            True, im.Composite((900, 1080), (0, 0), "images/sprites/normal/us/us_1_body.png", (0, 0), "images/sprites/normal/us/us_1_sport.png", (0, 0), "SovietDays/res/image/sprites/normal/us/us_1_bear.png", (0, 0), "images/sprites/normal/us/us_1_normal.png"))
    
    image us sad sport bear = ConditionSwitch(
            "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "images/sprites/normal/us/us_1_body.png", (0, 0), "images/sprites/normal/us/us_1_sport.png", (0, 0), "SovietDays/res/image/sprites/normal/us/us_1_bear.png", (0, 0), "images/sprites/normal/us/us_1_sad.png"), im.matrix.tint(0.94, 0.82, 1.0)),
            "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "images/sprites/normal/us/us_1_body.png", (0, 0), "images/sprites/normal/us/us_1_sport.png", (0, 0), "SovietDays/res/image/sprites/normal/us/us_1_bear.png", (0, 0), "images/sprites/normal/us/us_1_sad.png"), im.matrix.tint(0.63, 0.78, 0.82)),
            True, im.Composite((900, 1080), (0, 0), "images/sprites/normal/us/us_1_body.png", (0, 0), "images/sprites/normal/us/us_1_sport.png", (0, 0), "SovietDays/res/image/sprites/normal/us/us_1_bear.png", (0, 0), "images/sprites/normal/us/us_1_sad.png"))
    
    image us smile sport bear = ConditionSwitch(
            "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "images/sprites/normal/us/us_1_body.png", (0, 0), "images/sprites/normal/us/us_1_sport.png", (0, 0), "SovietDays/res/image/sprites/normal/us/us_1_bear.png", (0, 0), "images/sprites/normal/us/us_1_smile.png"), im.matrix.tint(0.94, 0.82, 1.0)),
            "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "images/sprites/normal/us/us_1_body.png", (0, 0), "images/sprites/normal/us/us_1_sport.png", (0, 0), "SovietDays/res/image/sprites/normal/us/us_1_bear.png", (0, 0), "images/sprites/normal/us/us_1_smile.png"), im.matrix.tint(0.63, 0.78, 0.82)),
            True, im.Composite((900, 1080), (0, 0), "images/sprites/normal/us/us_1_body.png", (0, 0), "images/sprites/normal/us/us_1_sport.png", (0, 0), "SovietDays/res/image/sprites/normal/us/us_1_bear.png", (0, 0), "images/sprites/normal/us/us_1_smile.png"))

    image sh shocked pioneer = ConditionSwitch(
            "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "images/sprites/normal/sh/sh_2_body.png", (0, 0), "SovietDays/res/image/sprites/normal/sh/sh_2_shocked.png"), im.matrix.tint(0.94, 0.82, 1.0)),
            "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "images/sprites/normal/sh/sh_2_body.png", (0, 0), "SovietDays/res/image/sprites/normal/sh/sh_2_shocked.png"), im.matrix.tint(0.63, 0.78, 0.82)),
            True, im.Composite((900, 1080), (0, 0), "images/sprites/normal/sh/sh_2_body.png", (0, 0), "SovietDays/res/image/sprites/normal/sh/sh_2_shocked.png"))
        