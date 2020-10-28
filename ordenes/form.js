var vents = {
    items: {
        fecha_out: '',
        gasto: 0,
        cobro: 0,
        total: 0,
    },
    calculate_invoice: function () {
        var gasto = 0;
        var cobro = 0;
        $.each(this.items, function (pos, dict) {
            dict.pos = pos;
            dict.gasto = dict.cant * parseFloat(dict.pvp);
            gasto += dict.gasto;
        });
        this.items.gasto = gasto;
        this.items.cobro = cobro;
        this.items.total = this.items.cobro - this.items.gasto;

        $('input[name="gasto"]').val(this.items.gasto.toFixed(2));
        $('input[name="cobro"]').val(this.items.cobro.toFixed(2));
        $('input[name="total"]').val(this.items.total.toFixed(2));
    },

};