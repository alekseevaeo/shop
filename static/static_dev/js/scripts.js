$(document).ready(function () { //работа с корзиной
    var form = $('#form_buying_product');
    console.log(form);

    function basketupdating(product_id, numb, is_delete) {
        var data = {};
        data.product_id = product_id;
        data.nmb = numb;
        var csrf_token = $('#form_buying_product [name="csrfmiddlewaretoken"]').val();
        data["csrfmiddlewaretoken"] = csrf_token;

        if(is_delete){
            data["is_delete"] = true
        }

        var url = form.attr("action");

        console.log(data);
        $.ajax({
            url: url,
            type: 'POST',
            data: data,
            cache: true,
            success: function (data) {
                console.log("OK");
                console.log(data.product_total_numb);
                if (data.product_total_numb || data.product_total_numb == 0) {
                    $('#product_total_numb').text("(" + data.product_total_numb + ")");
                    console.log(data.products);
                    $('.basket-items ul').html("");
                    $.each(data.products, function (k, v) {
                        $('.basket-items ul').append('<li><h6>' + v.name + ', ' + v.numb + 'шт. ' + 'по ' + v.price_per_item + ' руб  ' +
                            '<a class="delete-item" href="" data-product_id="'+v.id+'">x</a>' + //  href always must to be href="" data-product_id="'+v.id+'"
                            '</h6></li>');
                    });
                    $('.basket-items ul').append('                                <form>\n' +
                        '                                    <input class="btn btn-success" type="button" value="Оформить заказ"\n' +
                        '                                           onclick="javascript:window.location=\'/checkout\'"/>\n' +
                        '                                </form>');
                    if (data.product_total_numb == 0) {
                        $('.basket-items ul').html("");
                        $('.basket-items ul').append('<h4 >      Корзина пуста!</h4>');
                    }
                }
            },
            error: function () {
                console.log("ERROR")
            }
        });
    }

    form.on('submit', function (e) {
        e.preventDefault();
        console.log('123rus');
        var numb = $('#product_page_number').val();
        console.log(numb);
        var submite_btn = $('#product_submit_btn');
        var product_id = submite_btn.data("product_id");
        var product_name = submite_btn.data("product_name");
        var product_price = submite_btn.data("product_price");
        console.log(product_id);
        console.log(product_name);
        console.log(product_price);

        basketupdating(product_id, numb, is_delete=false)

    });
    $(document).on('click', '.delete-item', function (e) {
        e.preventDefault();
        product_id = $(this).data("product_id");
        numb = 0;
        basketupdating(product_id, numb, is_delete=true)
    });

    function calculatingBasketAmount() {
        var total_order_amount = 0;
        $('.total-product-in-basket-amount').each(function () {
            total_order_amount = total_order_amount + parseFloat($(this).text());
        });
        console.log(total_order_amount);
        $('#total_order_amount').text(total_order_amount.toFixed(2));
    }

    $(document).on('change', ".product-in-basket-nmb", function () {
        var current_nmb = $(this).val();
        console.log(current_nmb);

        var current_tr = $(this).closest('tr');
        var current_price = parseFloat(current_tr.find('.product-price').text()).toFixed(2);
        console.log(current_price);
        var total_amount = parseFloat(current_nmb * current_price).toFixed(2);
        console.log(total_amount);
        current_tr.find('.total-product-in-basket-amount').text(total_amount);

        calculatingBasketAmount();
    });


    calculatingBasketAmount();
});