var socket = io();

socket.on('connect', function() {
  console.log("Websocket connected.")
});

const size = 100

var manager = nipplejs.create({
  zone: document.getElementById('joystick'),
  color: 'green',
  mode: 'dynamic',
  size: size
});

manager.on('added', function (evt, nipple) {
  x = nipple.position.x;
  y = nipple.position.y;
}).on('move', function (evt, nipple) {
  dx = nipple.position.x - x;
  dy = y - nipple.position.y;

  dx = dx * 200 / size
  dy = dy * 200 / size

  socket.emit('steering-command', {x: dx, y: dy});
});