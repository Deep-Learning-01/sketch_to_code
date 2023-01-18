def get_checkbox(**kwargs):
    print("checkbox...")
    with kwargs['add'].div(klass="form-check"):
        kwargs['add'].input(klass="form-check-input", type="checkbox", id="sample_check1", name="sample_check1")
        string = ['<label class="form-check-label" for="sample_check1">', kwargs['text'], '</label>']
        # kwargs['add']._doc_elements.append(i)
        for i in string:
            kwargs['add']._doc_elements.append(i)


def get_button(**kwargs):
    print("button...")
    kwargs['add'].button(type="button", klass="btn btn-primary px-3", _t=kwargs['text'])


def get_carousel():
    string = ['<div class="container">',
              '<div id="carousel" class="carousel slide" data-ride="carousel" style="height:150px; width:200px">',
              '<a class="left carousel-control" href="#carousel" data-slide="prev">',
              '<span class="glyphicon glyphicon-chevron-left"></span>',
              '<span class="sr-only">Previous</span>', '</a>',
              '<a class="right carousel-control" href="#carousel" data-slide="next">',
              '<span class="glyphicon glyphicon-chevron-right"></span>', '<span class="sr-only">Next</span>', '</a>',
              '<ol class="carousel-indicators">', '<li data-target="#carousel" data-slide-to="0" class="active"></li>',
              '<li data-target="#carousel" data-slide-to="1"></li>',
              '<li data-target="#carousel" data-slide-to="2"></li>', '</ol>',
              '<div class="carousel-inner" >', '<div class="item active">',
              '<img src="https://www.iconsdb.com/icons/preview/gray/image-file-xxl.png" '
              'class="d-block w-100" alt="Any alternative" >',
              '</div>',
              '<div class="item">', '<img src="https://www.iconsdb.com/icons/preview/gray/image-file-xxl.png"'
                                    ' class="d-block w-100" alt="Any alternative" >',
              '</div>',
              '<div class="item">', '<img src="https://www.iconsdb.com/icons/preview/gray/image-file-xxl.png"'
                                    ' class="d-block w-100" alt="Any alternative" >',
              '</div>',
              '<a class="left carousel-control" href="#myCarousel" data-slide="prev">',
              '<span class="glyphicon glyphicon-chevron-left"></span>',
              '<span class="sr-only">Previous</span>', '</a>',
              '<a class="right carousel-control" href="#myCarousel" data-slide="next">',
              '<span class="glyphicon glyphicon-chevron-right"></span>', '<span class="sr-only">Next</span>', '</a>',
              '</div>', '</div>', '</div>']
    return string

def get_text(**kwargs):
    print("heading...")
    with kwargs['add'].p(klass="h4"):
        kwargs['add'](kwargs['text'])

def get_heading(**kwargs):
    print("heading...")
    with kwargs['add'].p(klass="h2"):
        kwargs['add'](kwargs['text'])


def get_headings_top(**kwargs):
    print("heading...")
    with kwargs['add'].p(klass="h2"):
        kwargs['add'](kwargs['text'])


def get_image(**kwargs):
    print("image...")
    kwargs['add'].img(src="https://www.iconsdb.com/icons/preview/gray/image-file-xxl.png", klass="img-fluid mt-4",
                      alt="Image will be here")


def get_label(**kwargs):
    print("label...")
    with kwargs['add'].label():
        kwargs['add'](kwargs['text'])


def get_link(**kwargs):
    print("link...")
    with kwargs['add'].a(href="#", klass="stretched-link"):
        kwargs['add'](kwargs['text'])


def get_pagination(**kwargs):
    print("pagination...")
    with kwargs['add'].ul(klass="pagination"):
        with kwargs['add'].li(klass="page-item"):
            kwargs['add'].a(klass="page-item", href="#", _t="Previous")
        with kwargs['add'].li(klass="page-item"):
            kwargs['add'].a(klass="page-item", href="#", _t="1")
        with kwargs['add'].li(klass="page-item"):
            kwargs['add'].a(klass="page-item", href="#", _t="2")
        with kwargs['add'].li(klass="page-item"):
            kwargs['add'].a(klass="page-item", href="#", _t="3")
        with kwargs['add'].li(klass="page-item"):
            kwargs['add'].a(klass="page-item", href="#", _t="Next")


def get_paragraph(**kwargs):
    print("paragraph...")
    with kwargs['add'].p(klass="text-black-50"):
        kwargs['add']("Lorem ipsum dolor sit amet, consectetur adipiscing elit \
        <br /> \
        sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. \
        <br /> \
        Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris")


def get_radio_button(**kwargs):
    print("radio_button...")
    with kwargs['add'].div(klass="form-check"):
        kwargs['add'].input(type="radio", klass="form-check-input", name="radio_button1", id="radio_button1")
        string = ['<label class="form-check-label" for="sample_check1">', kwargs['text'], '</label>']
        # add._doc_elements.append(i)
        for i in string:
            kwargs['add']._doc_elements.append(i)


def get_select(**kwargs):
    print("select...")
    with kwargs['add'].select(klass="form-select"):
        kwargs['add'].option(value="0", _t="Select your choice")
        kwargs['add'].option(value="1", _t="OptionOne")
        kwargs['add'].option(value="2", _t="OptionTwo")
        kwargs['add'].option(value="3", _t="OptionThree")


def get_table(**kwargs):
    print("table...")
    with kwargs['add'].table():
        with kwargs['add'].thead().tr():
            kwargs['add'].th(scope="col", _t="#")
            kwargs['add'].th(scope="col")
            kwargs['add'].th(scope="col")
            kwargs['add'].th(scope="col")
        with kwargs['add'].tbody():
            with kwargs['add'].tr():
                kwargs['add'].th(scope="row", _t="1")
                kwargs['add'].td()
                kwargs['add'].td()
                kwargs['add'].td()
                kwargs['add'].th(scope="row", _t="1")
                kwargs['add'].td()
                kwargs['add'].td()
                kwargs['add'].td()
            with kwargs['add'].tr():
                kwargs['add'].th(scope="row", _t="3")
                kwargs['add'].td(colspan="2")
                kwargs['add'].td()


def get_text_area(**kwargs):
    print("textarea...")
    kwargs['add'].textarea(rows="9", cols="40")


def get_text_box(**kwargs):
    print("textbox...")

    kwargs['add'].input(type='text', name="sample_textbox")


actions = [get_text, get_button, None, get_checkbox, get_heading, get_image, get_label, get_link, get_pagination,
           get_paragraph, get_radio_button, get_select, get_table, get_text_area, get_text_box]


def get_elements(add, label, text="No value"):
    if label == 2:
        string = get_carousel()
        for i in string:
            add._doc_elements.append(i)
        return
    actions[label](add=add, text=text)
