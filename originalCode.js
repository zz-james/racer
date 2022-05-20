const makeRandomTerrain = function () {
  var basey = 250;
  var x = 0;
  var ang = 0;
  var hei = basey - 220;
  var pit = 0;
  var lastpit = 0;
  var boulderCount = 0;

  ground.clear();
  ground.moveTo(x, basey);
  ground.beginFill(0x915039);

  ground.createEmptyMovieClip("objs", 1);

  _root.waterMC.removeMovieClip();
  _root.createEmptyMovieClip("waterMC", _root.getNextHighestDepth());
  waterMC._y = 295;

  var steps = 0;

  while (x < 15100) {
    var wid = Math.random() * 100 + 50;

    hei += Math.sin(ang) * wid;
    ang += Math.random() * 2 - 1;

    if (pit > 0) {
      hei = basey + 300;
      pit--;
    } else if (hei < -100) {
      hei = -100;
      ang = 0.1;
    } else if (hei > basey - 100) {
      hei = basey - 100;
      ang = -0.1;
    }

    if (lastpit > 0) lastpit--;

    if (Math.random() < 0.033 && pit == 0 && x > 700 && lastpit == 0) {
      // begin a pit
      pit = Math.floor(Math.random() * 3) + 3;
      lastpit = pit + 5;

      // Create a small ramp
      hei = ohei - 40;
    }

    // Choose between a flat ground segment or a
    // curved segment
    if (random(10) > 5) {
      x += wid;
      ground.lineTo(x, hei);
    } else {
      ground.curveTo(x + wid / 2, hei + ang * 10, x + wid, hei);
      x += wid;
    }

    if (Math.random() < 0.1 && ang > -0.1 && x > 500 && x < 14000) {
      var nm = "bldr" + boulderCount;
      ground.objs.attachMovie("trackObjects", nm, boulderCount);
      ground.objs[nm]._x = x;
      ground.objs[nm]._y = hei + 10;
      ground.objs[nm].gotoAndStop(Math.floor(Math.random() * 4) + 1);
      boulderCount++;
    }

    if (steps % 25 == 20) {
      var nm = "drop" + waterMC.getNextHighestDepth();
      waterMC.attachMovie("waterDrop", nm, waterMC.getNextHighestDepth());
      waterMC[nm]._x = x;
      waterMC[nm]._y = hei + 2;
    }

    steps++;
    ohei = hei;
  }

  var nm = "finisher";
  ground.objs.attachMovie("trackObjects", nm, boulderCount);
  ground.objs[nm]._x = x - 600;
  ground.objs[nm]._y = hei + 10;
  ground.objs[nm].gotoAndStop(6);

  ground.lineTo(x, basey + 400);
  ground.lineTo(0, basey + 400);
  ground.endFill();

  lastGet = 0;
};

function showlives() {
  lives_txt.text = lives;
}

function wheelControl() {
  this._y += this.dy; // what is this here??  -- move the wheel by by

  accelerating = false;

  if (Key.isDown(Key.RIGHT) && oneOnGround) {
    this.dx += 0.3;
    mydir = 1;
    accelerating = true;
  }
  if (Key.isDown(Key.LEFT) && oneOnGround) {
    this.dx -= 0.3;
    mydir = -1;
    accelerating = true;
  }

  if (accelerating && Math.abs(this.dx) < 2) {
    enginerev.start(0, 0);
  }

  if (oneOnGround) this.dx *= 0.98;
  this.dy += 0.5;

  if (ground.hitTest(this._x, this._y, true)) {
    var ty = this._y;
    var cnt = 0;
    while (ground.hitTest(this._x, ty, true)) {
      ty--;
      cnt++;
    }

    if (cnt > 70) {
      // Hit a Wall
      wheel0.dx *= -1;
      wheel1.dx *= -1;
      ground._x -= this.dx;
      crash.start(0, 0);
    } else {
      if (cnt < 5) cnt = 0;
      this._y = ty;
      this.dy += -cnt / 3;
      this.onGround = true;
    }
  } else this.onGround = false;

  if (this.dy > 15) this.dy = 15;
  if (this.dy < -15) this.dy = -15;
}

wheel1.dx = 0;
wheel1.dy = 0;
wheel1.onEnterFrame = wheelControl;

wheel0.dx = 0;
wheel0.dy = 0;
wheel0.onEnterFrame = wheelControl;

_quality = "MEDIUM";

ground.onEnterFrame = function () {
  this._x -= wheel1.dx;
  waterMC._x = this._x;

  minicar._x = (-this._x / this._width) * 640;

  if (this._x > 0) {
    this._x = 0;
    wheel1.dx = 0;
    wheel0.dx = 0;
  }

  if (wheel1._y > 600) {
    if (lives == 0) {
      endClip._visible = true;
      endClip.gotoAndStop(2);
      delete wheel0.onEnterFrame;
      delete wheel1.onEnterFrame;
      delete this.onEnterFrame;
      delete car.onEnterFrame;
      return false;
    }

    // Fall to Death in a Pit
    wheel1._y = 100;
    wheel1.dx = 0;
    wheel1.dy = 0;

    wheel0._y = 100;
    wheel0.dx = 0;
    wheel0.dy = 0;

    this._x = 0;
    fall.start(0, 0);

    lives--;

    showlives();
  }

  if (-this._x > this.objs.finisher._x) {
    // Pass the Finish line
    wheel1._y = 100;
    wheel1.dx = 0;
    wheel1.dy = 0;

    wheel0._y = 100;
    wheel0.dx = 0;
    wheel0.dy = 0;

    this._x = 0;
    makeRandomTerrain();
  }
};

ground._x = 0;
ground._y = 295;

ground.c = new Color(ground);
ground.t = new Object();
ground.t.ra = 100;
ground.t.ga = 100;
ground.t.ba = 100;
ground.t.rb = 0;
ground.t.gb = 0;
ground.t.bb = 0;

sky.c = new Color(sky);
sky.t = new Object();
sky.t.ra = 100;
sky.t.ga = 100;
sky.t.ba = 100;
sky.t.rb = 0;
sky.t.gb = 0;
sky.t.bb = 0;

function setWetLevel(lvl) {
  ground.t.ra = 100 - 66 * lvl;
  ground.t.gb = 66 * lvl;
  ground.t.bb = 12 * lvl;

  sky.t.ra = 100 - 66 * lvl;
  sky.t.rb = 66 * lvl;
  sky.t.gb = 56 * lvl;
  sky.t.bb = 132 * lvl;

  ground.c.setTransform(ground.t);
  sky.c.setTransform(sky.t);

  waterMeter._yscale = lvl * 100;
}

function myOnKeyDown() {
  if (Key.isDown(Key.CONTROL) && oneOnGround) {
    bounce.start(0, 0);
    if (mydir == -1) {
      wheel0.dy = -11;
      wheel1.dy = -10;
    } else {
      wheel0.dy = -10;
      wheel1.dy = -11;
    }
  }
}

var myListener = new Object();
myListener.onKeyDown = myOnKeyDown;
Key.addListener(myListener);

car.onEnterFrame = function () {
  var midy = (wheel1._y + wheel0._y) / 2;

  this._x = 189.1;
  this._y = midy;

  var diffx = wheel1._x - wheel0._x;
  var diffy = wheel1._y - wheel0._y;

  var ang = Math.atan2(diffy, diffx);

  this._rotation = 180 * (ang / Math.PI);
  wheel0._rotation = this._rotation + 40;
  wheel1._rotation = this._rotation - 40;

  allOnGround = wheel0.onGround & wheel1.onGround;
  oneOnGround = wheel0.onGround | wheel1.onGround;

  if (allOnGround && !accelerating && (ang < -0.1 || ang > 0.1)) {
    // Natural roll downhill
    wheel0.dx += ang / 2;
    wheel1.dx += ang / 2;
  }

  if (ang < -1.4) ang = -1.4;
  if (ang > 1.4) ang = 1.4;

  var dist = Math.sqrt(diffx * diffx + diffy * diffy);

  if (dist > 61 || dist < 58) {
    wheel0._x = this._x - Math.cos(ang) * 30;
    wheel0._y = this._y - Math.sin(ang) * 30;

    wheel1._x = this._x + Math.cos(ang) * 30;
    wheel1._y = this._y + Math.sin(ang) * 30;
  }

  this._xscale = mydir * 153.8;

  if (waterMC.hitTest(this._x, this._y, true)) {
    for (var i = lastGet; i < waterMC.getNextHighestDepth(); i++) {
      if (waterMC["drop" + i].hitTest(this._x, this._y, true)) {
        waterMC["drop" + i].removeMovieClip();
        lastGet = i + 1;
        gWetLevel += 0.02;
        setWetLevel(gWetLevel);
        lives++;
        showlives();

        if (gWetLevel >= 1) {
          endClip._visible = true;
          endClip.gotoAndStop(1);
          delete wheel0.onEnterFrame;
          delete wheel1.onEnterFrame;
          delete ground.onEnterFrame;
          delete this.onEnterFrame;
        }

        break;
      }
    }
  }
};

mainsong = new Sound();
mainsong.attachSound("song");
mainsong.setVolume(50);
mainsong.start(0, 99999);

crash = new Sound();
crash.attachSound("crash");

fall = new Sound();
fall.attachSound("fall");

bounce = new Sound();
bounce.attachSound("bounce");

enginerev = new Sound(car);
enginerev.attachSound("enginerev");

engineloop = new Sound(car);
engineloop.attachSound("engineloop");
engineloop.start(0, 99999);
engineloop.setVolume(50);

gWetLevel = 0;
makeRandomTerrain();
setWetLevel(gWetLevel);
lives = 10;
showlives();

endClip._visible = false;
endClip.stop();
