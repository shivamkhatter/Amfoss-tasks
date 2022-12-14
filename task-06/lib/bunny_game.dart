import 'dart:ui';

import 'package:flame/game.dart';
import 'package:flame_game/bunny_player.dart';
import 'package:flame_game/bunny_world.dart';
import 'bunny_player.dart';
import 'bunny_world.dart';
import 'directions.dart';

class bunnygame extends FlameGame{
  bunnyplayer _bunnyplayer = bunnyplayer();
  bunnyworld _bunnyworld = bunnyworld();
  @override
  Future<void> onLoad() async {
    super.onLoad();
    await add(_bunnyworld);
    await add(_bunnyplayer);
    _bunnyplayer.position = _bunnyworld.size / 1.5;
    camera.followComponent(_bunnyplayer,
        worldBounds: Rect.fromLTRB(0, 0, _bunnyworld.size.x, _bunnyworld.size.y));
  }

  onArrowKeyChanged(Direction direction){
    _bunnyplayer.direction = direction;
  }
}