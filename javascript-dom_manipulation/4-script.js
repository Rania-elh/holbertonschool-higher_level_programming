document.getElementById('add_item').onclick = function() {
	document.querySelector('UL.my_list').appendChild(document.createElement('li')).textContent = 'Item';
}
