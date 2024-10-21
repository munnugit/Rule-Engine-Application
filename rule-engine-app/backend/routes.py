from flask import Blueprint, request, jsonify
from ast_processor import parse_rule_string, combine_rules, evaluate_ast
from models import Rule
from database import SessionLocal

rule_blueprint = Blueprint("rules", __name__)

@rule_blueprint.route("/api/create_rule", methods=["POST"])
def create_rule():
    data = request.json
    rule_string = data.get("rule")
    rule_ast = parse_rule_string(rule_string)
    session = SessionLocal()
    new_rule = Rule(name=data.get("name"), rule_ast=rule_ast)
    session.add(new_rule)
    session.commit()
    return jsonify({"message": "Rule created successfully", "rule_id": new_rule.id})

@rule_blueprint.route("/api/combine_rules", methods=["POST"])
def combine_rules_api():
    data = request.json
    rule_ids = data.get("rule_ids")
    session = SessionLocal()
    rule_asts = [session.query(Rule).filter(Rule.id == rule_id).first().rule_ast for rule_id in rule_ids]
    combined_ast = combine_rules(rule_asts)
    return jsonify({"combined_rule_ast": combined_ast})

@rule_blueprint.route("/api/evaluate_rule", methods=["POST"])
def evaluate_rule():
    data = request.json
    rule_id = data.get("rule_id")
    user_data = data.get("user_data")
    session = SessionLocal()
    rule = session.query(Rule).filter(Rule.id == rule_id).first()
    if not rule:
        return jsonify({"error": "Rule not found"}), 404
    result = evaluate_ast(rule.rule_ast, user_data)
    return jsonify({"result": result})
