$('.ui.dropdown')
    .dropdown()
;

$('.ui.form')
    .form({
        fields: {
            text_main: {
                identifier: 'text[main]',
                rules: [
                    {
                        type: 'empty',
                        prompt: 'Please enter some main text'
                    }
                ]
            },
            text_wrapper: {
                identifier: 'text[wrapper]',
                rules: [
                    {
                        type: 'empty',
                        prompt: 'Please enter some wrapper text'
                    }
                ]
            }
        }
    })
;