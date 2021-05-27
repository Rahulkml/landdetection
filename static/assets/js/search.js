const user_input = $("#user-input")
const search_icon = $('#search-icon')
const artists_div = $('#replaceable-content')
const user_input2 = $("#user-input2")
const search_icon2 = $('#search-icon2')
const artists_div2 = $('#replaceable-content2')
const user_input3 = $("#user-input3")
const search_icon3 = $('#search-icon3')
const artists_div3 = $('#replaceable-content3')
const endpoint = '/app/search/'
const endpoint2 = '/app/cards/'
const endpoint3 = '/app/customers/'
const delay_by_in_ms = 500
let scheduled_function = false


let ajax_call = function (endpoint, request_parameters) {
	$.getJSON(endpoint, request_parameters)
		.done(response => {
			// fade out the artists_div, then:
			artists_div.fadeTo('slow', 0).promise().then(() => {
				// replace the HTML contents
				artists_div.html(response['html_from_view'])
				// fade-in the div with new contents
				artists_div.fadeTo('slow', 1)
				// stop animating search icon
				search_icon.removeClass('blink')
			})
		})
}


user_input.on('keyup', function () {

	const request_parameters = {
		q: $(this).val() // value of user_input: the HTML element with ID user-input
	}

	// start animating the search icon with the CSS class
	search_icon.addClass('blink')

	// if scheduled_function is NOT false, cancel the execution of the function
	if (scheduled_function) {
		clearTimeout(scheduled_function)
	}

	// setTimeout returns the ID of the function to be executed
	scheduled_function = setTimeout(ajax_call, delay_by_in_ms, endpoint, request_parameters)
})

// ------------------------------------------------------

let ajax_call2 = function (endpoint2, request_parameters) {
	$.getJSON(endpoint2, request_parameters)
		.done(response => {
			// fade out the artists_div, then:
			artists_div2.fadeTo('slow', 0).promise().then(() => {
				// replace the HTML contents
				artists_div2.html(response['html_from_view'])
				// fade-in the div with new contents
				artists_div2.fadeTo('slow', 1)
				// stop animating search icon
				search_icon2.removeClass('blink')
			})
		})
}


user_input2.on('keyup', function () {

	const request_parameters = {
		q: $(this).val() // value of user_input: the HTML element with ID user-input
	}

	// start animating the search icon with the CSS class
	search_icon2.addClass('blink')

	// if scheduled_function is NOT false, cancel the execution of the function
	if (scheduled_function) {
		clearTimeout(scheduled_function)
	}

	// setTimeout returns the ID of the function to be executed
	scheduled_function = setTimeout(ajax_call2, delay_by_in_ms, endpoint2, request_parameters)
})

// ------------------------------------------------------

let ajax_call3 = function (endpoint3, request_parameters) {
	$.getJSON(endpoint3, request_parameters)
		.done(response => {
			// fade out the artists_div, then:
			artists_div3.fadeTo('slow', 0).promise().then(() => {
				// replace the HTML contents
				artists_div3.html(response['html_from_view'])
				// fade-in the div with new contents
				artists_div3.fadeTo('slow', 1)
				// stop animating search icon
				search_icon3.removeClass('blink')
			})
		})
}


user_input3.on('keyup', function () {

	const request_parameters = {
		q: $(this).val() // value of user_input: the HTML element with ID user-input
	}

	// start animating the search icon with the CSS class
	search_icon3.addClass('blink')

	// if scheduled_function is NOT false, cancel the execution of the function
	if (scheduled_function) {
		clearTimeout(scheduled_function)
	}

	// setTimeout returns the ID of the function to be executed
	scheduled_function = setTimeout(ajax_call3, delay_by_in_ms, endpoint3, request_parameters)
})