# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp.osv import fields, osv
import pdb

class stock_picking_out(osv.osv):
    _name = 'stock.picking.out'
    _inherit = 'stock.picking.out'
  
    def _fnct_picking_invoice(self, cr, uid, ids, field_name, args, context=None):
        sale_order_obj = self.pool.get('sale.order')
	invoice_obJ = self.pool.get('account.invoice')
        if context is None:
            context = {}
        res = {}
	for picking in picking_obj.browse(cr,uid,picking_ids):
		invoice_obJ = self.pool.get('account.invoice')
		invoice_ids = invoice_obj.search(cr,uid,[('origin','=',picking.sale_id.name)])
		if invoice_ids:
			for invoice in invoice_obj.browse(cr,uid,invoice_ids):
				res[picking.id] = invoice.number
		else:
			res[picking.id] = ''

        return res

    _columns = {
        'invoice_number': fields.function(_fnct_picking_invoice, string='Invoice number'),
    }

stock_picking_out()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
