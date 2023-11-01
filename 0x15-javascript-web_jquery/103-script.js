document.addEventListener('DOMContentLoaded', function () {
    $('#btn_translate').click(function () {
      const languageCode = $('#language_code').val();
      const apiUrl = `https://www.fourtonfish.com/hellosalut/hello/?lang=${languageCode}`;
  
      $.get(apiUrl, function (data) {
        const translation = data.hello;
        $('#hello').text(translation);
      });
    });
  });