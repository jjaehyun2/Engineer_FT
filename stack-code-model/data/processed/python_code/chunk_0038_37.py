package {
  import flash.utils.ByteArray;

  (function () {
  	var data = new ByteArray();

  	data.writeUTFBytes('Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc hendrerit, risus vel dapibus hendrerit, augue ipsum adipiscing lorem, quis orci aliquam.');
  	trace(data.length);

  	data.deflate();
  	trace(data.length !== 150);

  	data.inflate();
  	trace(data.length);

  	trace(data.readUTFBytes(150));
  })();
}