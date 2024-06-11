import odoo
from odoo import api, SUPERUSER_ID
from odoo.tools import config

def populate_data():
    db_name = 'test'
    with odoo.registry(db_name).cursor() as cr:
        env = api.Environment(cr, SUPERUSER_ID, {})

        denim_fabric = env['product.ingredient'].create({
            'name': 'Denim Fabric',
            'quantity': 1.5,
            'unit': 'm x 140cm'
        })
        siege_band = env['product.ingredient'].create({
            'name': 'Siege band',
            'quantity': 1,
            'unit': 'H180'
        })
        zipper = env['product.ingredient'].create({
            'name': 'Zipper',
            'quantity': 1,
            'unit': '16cm'
        })
        stitching_yarn = env['product.ingredient'].create({
            'name': 'Stitching yarn',
            'quantity': 40,
            'unit': 'm'
        })
        pattern_paper = env['product.ingredient'].create({
            'name': 'Pattern paper',
            'quantity': 0.01,
            'unit': 'pattern paper 1.50m x 140cm'
        })
        button = env['product.ingredient'].create({
            'name': 'Button',
            'quantity': 1,
            'unit': 'unit'
        })
        nails = env['product.ingredient'].create({
            'name': 'Nails',
            'quantity': 8,
            'unit': 'units'
        })
        labels = env['product.ingredient'].create({
            'name': 'Labels',
            'quantity': 3,
            'unit': 'units'
        })
        price_tag = env['product.ingredient'].create({
            'name': 'Price tag',
            'quantity': 1,
            'unit': 'unit'
        })
        cord = env['product.ingredient'].create({
            'name': 'Cord',
            'quantity': 20,
            'unit': 'cm'
        })
        pvc_sac = env['product.ingredient'].create({
            'name': 'PVC sac',
            'quantity': 1,
            'unit': 'unit'
        })
        plastic_bale = env['product.ingredient'].create({
            'name': 'Plastic bale',
            'quantity': 0.025,
            'unit': 'unit'
        })
        tape = env['product.ingredient'].create({
            'name': 'Tape',
            'quantity': 0.025,
            'unit': '20cm'
        })

        denim_fabric_component = env['product.component'].create({
            'name': 'Denim Fabric',
            'country_of_origin': 'India',
            'emissions': '2 kg CO2e',
            'ingredients': [(6, 0, [denim_fabric.id])]
        })
        haberdashery_subcomponents = [
            env['product.component'].create({
                'name': 'Haberdashery',
                'country_of_origin': 'China',
                'emissions': '0.5 kg CO2e',
                'ingredients': [(6, 0, [siege_band.id, zipper.id])]
            }),
            env['product.component'].create({
                'name': 'Yarn',
                'country_of_origin': 'Vietnam',
                'emissions': '0.3 kg CO2e',
                'ingredients': [(6, 0, [stitching_yarn.id])]
            }),
            env['product.component'].create({
                'name': 'Pattern Paper',
                'country_of_origin': 'Germany',
                'emissions': '0.1 kg CO2e',
                'ingredients': [(6, 0, [pattern_paper.id])]
            })
        ]
        jeans_sewed = env['product.component'].create({
            'name': 'Jeans Sewed',
            'country_of_origin': 'Turkey',
            'emissions': '1.5 kg CO2e',
            'subcomponents': [(6, 0, [denim_fabric_component.id] + [comp.id for comp in haberdashery_subcomponents])]
        })
        jeans_washed = env['product.component'].create({
            'name': 'Jeans Washed',
            'country_of_origin': 'Italy',
            'emissions': '1 kg CO2e',
            'subcomponents': [(6, 0, [jeans_sewed.id])]
        })
        haberdashery = env['product.component'].create({
            'name': 'Haberdashery',
            'country_of_origin': 'France',
            'emissions': '0.2 kg CO2e',
            'ingredients': [(6, 0, [button.id, nails.id])]
        })
        labels_component = env['product.component'].create({
            'name': 'Labels',
            'country_of_origin': 'Portugal',
            'emissions': '0.1 kg CO2e',
            'ingredients': [(6, 0, [labels.id, price_tag.id, cord.id])]
        })
        jeans_complete = env['product.component'].create({
            'name': 'Jeans Complete',
            'country_of_origin': 'Bangladesh',
            'emissions': '3 kg CO2e',
            'subcomponents': [(6, 0, [jeans_washed.id, haberdashery.id, labels_component.id])]
        })
        packing_materials = env['product.component'].create({
            'name': 'Packing materials',
            'country_of_origin': 'Poland',
            'emissions': '0.5 kg CO2e',
            'ingredients': [(6, 0, [pvc_sac.id, plastic_bale.id, tape.id])]
        })
        jeans_packed = env['product.component'].create({
            'name': 'Jeans Packed',
            'country_of_origin': 'China',
            'emissions': '5 kg CO2e',
            'subcomponents': [(6, 0, [jeans_complete.id, packing_materials.id])]
        })

        product = env['product.template'].create({
            'name': 'Denim Jeans',
            'components': [(6, 0, [jeans_packed.id])]
        })

if __name__ == "__main__":
    config.parse_config(['--db_host=localhost', '--db_port=5432', '--db_user=odoo', '--db_password=odoo'])
    odoo.cli.server.setup()
    populate_data()
