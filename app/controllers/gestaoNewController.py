import json

# gestao/info
# gestao/orcamentos/vendedor
# gestao/orcamento

from app import db
from flask import jsonify
from sqlalchemy.orm import load_only
from app.models.gestaoNewModel import (
    Orcamento,
    orcamento_schema,
    orcamentos_schema,
    Pedido,
    pedido_schema,
    pedidos_schema,
    PedidoItem,
    pedidoitems_schema,
    OrcamentoItem,
    orcamentoitems_schema,
    )


def get_gestao_info_orcamentos():
    try:
        result = Orcamento.query.all()
        print(result)
    except Exception as err:
        print(err)
        return None

    result = orcamentos_schema.dump(result)

    return jsonify({'orcamentos': result}), 200


def get_gestao_info_orcamento(codigoOrcamento):
    if not codigoOrcamento.isnumeric():
        return jsonify({'error': 'Parametros Inválidos.'}), 400
    try:
        result = Orcamento.query.filter(Orcamento.CodigoOrcamento == codigoOrcamento).first()
        print(result)
    except Exception as err:
        print(err)
        return None

    if not result:
        return jsonify({'error': 'Parametros Inválidos.'}), 400

    orcamento = orcamento_schema.dump(result) if result else None
    return jsonify({'orcamento': orcamento})


# gestao/info
def get_gestao_info(codigoOrcamento):
    if not codigoOrcamento.isnumeric():
        return jsonify({'error': 'Parametros Inválidos.'}), 400

    try:
        result = db.session.query(Orcamento.CodigoOrcamento == codigoOrcamento)\
            .first()
    except Exception as err:
        print(err)
        return None

    if not result:
        return jsonify({"error": "Código informado inválido."}), 400

    orcamento = orcamentos_schema.dump(result) if result else None

    return jsonify({"orcamento": orcamento})


# gestao/orcamento
def get_orcamentos_idclient(idCliente):
    if not idCliente.isnumeric():
        return jsonify({"error": "Parametros Inválidos."}), 400

    try:
        result = Orcamento.query.filter(Orcamento.IdCliente == idCliente).all()
    except Exception as err:
        print(err)
        return None

    if not result:
        return jsonify({"message": "Não há orçamentos para esse ID."}), 404

    result = orcamentos_schema.dump(result)
    return jsonify({"orcamentos": result}), 200


def get_items_orcamento(idpedido):
    if not idpedido.isnumeric():
        return jsonify({"error": "Parametros Inválidos"}), 400
    try:
        result = OrcamentoItem.query.filter(OrcamentoItem.IdPedido == idpedido).all()
    except Exception as err:
        print(err)
        return None

    if not result:
        return jsonify({"message": "Não há items nesse orçamento."}), 404

    result = orcamentoitems_schema.dump(result)
    return jsonify({"items": result}), 200


def get_pedidos():
    try:
        result = Pedido.query.all()
    except Exception as err:
        print(err)
        return None

    result = pedidos_schema.dump(result)
    return jsonify({"pedidos": result}), 200


def get_pedidos_idclient(clienteid):
    if not clienteid.isnumeric():
        return jsonify({"error": "Parametros Inválidos."}), 400

    try:
        result = Pedido.query.filter(Pedido.cliente_id == clienteid).all()
    except Exception as err:
        print(err)
        return None

    if not result:
        return jsonify({"message": "Não há pedidos para esse ID."}), 404

    result = pedidos_schema.dump(result)
    return jsonify({"pedidos": result}), 200


def get_items_pedido(idpedido):
    if not idpedido.isnumeric():
        return jsonify({"error": "Parametros Inválidos"}), 400
    try:
        result = PedidoItem.query.filter(PedidoItem.IdPedido == idpedido).all()

    except Exception as err:
        print(err)
        return None

    if not result:
        return jsonify({"message": "Não há items nesse pedido."}), 404

    result = pedidoitems_schema.dump(result)
    return jsonify({"items": result}), 200

# gestao/orcamentos/vendedor
def get_orcamento_valor(idColaborador):
    fields = ('ValorTotal')
    if not idColaborador.isnumeric():
        return jsonify({"error": "Parametros Inválidos"}), 400
    try:
        result = Orcamento.query.filter(Orcamento.IdColaborador == idColaborador,
                                        Orcamento.IdStatusOrcamento not in (2, 3)) \
            .filter(Orcamento.IdColaborador == idColaborador)\
            .all()

        total = 0
        for i in result:
            orcamento_valor = orcamento_schema.dump(i) if i else None
            total += orcamento_valor['ValorTotal']
            #print(total)
        valor_total_orcamento = round(total, 2)


        #valor_total_avan = sum(result) if result else None
        #temp_list = []
        # result = db.session.query(Franqueados, Orcamento) \
        #     .join(Orcamento, Orcamento.IdPedido == Franqueados.IdOrcamentoGestao) \
        #     .filter(Franqueados.IdColaborador == idColaborador, Franqueados.IdPosicao == 4).all()
        #
        # for i in result:
        #     xd = orcamentos_schema.dump(i) if i else None
        #     temp_list.append(xd[1]['valor_total'])
        # valor_total_avan = sum(temp_list)
    except Exception as err:
        print(err)
        return None

    return jsonify({"valor_total": valor_total_orcamento}), 200
                    #"valor_total_avanc": valor_total_avan}), 200
