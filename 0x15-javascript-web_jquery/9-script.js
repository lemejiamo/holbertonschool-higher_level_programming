$.get('https://fourtonfish.com/hellosalut/?lang=fr', (data, textStatus) => {
		if (textStatus === 'success') {
			// const data = data.results
    $('DIV#hello').text(data.hello);
  }
});
