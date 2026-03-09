import json
import os
from datetime import datetime

class InvestorBunnyGenerator:
    def __init__(self, template_path, output_dir):
        self.template_path = template_path
        self.output_dir = output_dir
        with open(template_path, 'r') as f:
            self.template = f.read()

    def generate_report(self, data_json_path, report_type="swing"):
        with open(data_json_path, 'r') as f:
            market_data = json.load(f)
        
        quote = market_data.get('quote', {})
        inds = market_data.get('indicators', {}).get('indicators', {})
        hist = market_data.get('price_history', {})
        
        ticker = market_data.get('ticker', 'UNKNOWN')
        price = quote.get('price', 0)
        change_pct = quote.get('change_pct', 0)
        status_class = "bullish" if change_pct >= 0 else "bearish"
        direction_icon = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><polyline points="18 15 12 9 6 15"></polyline></svg>' if change_pct >= 0 else '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><polyline points="6 9 12 15 18 9"></polyline></svg>'
        
        range_52w_high = hist.get('52w_high', 1)
        range_52w_low = hist.get('52w_low', 0)
        range_pct = int(((price - range_52w_low) / (range_52w_high - range_52w_low)) * 100) if range_52w_high != range_52w_low else 0

        market_rows = f"<tr><td>Sector Matrix</td><td><span class='badge badge-bull'>Outperforming</span></td></tr><tr><td>Market Regime</td><td><span class='badge badge-neu'>Mixed</span></td></tr>"
        
        stat_items = f"""
            <div class='stat-item'><div class='stat-label'>EMA 50</div><div class='stat-value'>${inds.get('EMA50', 0):.2f}</div></div>
            <div class='stat-item'><div class='stat-label'>Vol Ratio</div><div class='stat-value'>{inds.get('Vol_ratio', 0):.2f}x</div></div>
        """

        technical_rows = f"<tr><td>EMA 50 Support</td><td>${inds.get('EMA50', 0):.2f}</td><td>Hold Base</td><td><span class='badge badge-bull'>Buy</span></td></tr>"

        target_items = f"""
            <li style='display: flex; justify-content: space-between;'><span style='background: rgba(101, 163, 13, 0.2); padding: 4px 10px; border-radius: 4px;'>T1</span><span style='font-family: Fraunces;'>${price*1.08:.2f}</span></li>
            <li style='display: flex; justify-content: space-between;'><span style='background: rgba(101, 163, 13, 0.2); padding: 4px 10px; border-radius: 4px;'>T2</span><span style='font-family: Fraunces;'>${price*1.15:.2f}</span></li>
        """

        replacements = {
            "{{COMPANY_NAME}}": ticker,
            "{{REPORT_SUBTITLE}}": f"{report_type.upper()} Intelligence",
            "{{CURRENT_PRICE}}": f"${price:.2f}",
            "{{PRICE_STATUS_CLASS}}": status_class,
            "{{CHANGE_DIRECTION_ICON}}": direction_icon,
            "{{CHANGE_PERCENTAGE}}": f"{abs(change_pct):.2f}%",
            "{{THESIS_SENTIMENT}}": "High Conviction",
            "{{THESIS_TITLE}}": f"{ticker} Multi-Cycle Breakout",
            "{{THESIS_CONTENT}}": f"Strategic accumulation signature on {ticker} near key pivot around ${inds.get('EMA50', 0):.2f}.",
            "{{GROWTH_SCORE}}": "9.2/10",
            "{{TECHNICAL_SCORE}}": "8.8/10",
            "{{MARKET_TABLE_ROWS}}": market_rows,
            "{{STAT_ITEMS}}": stat_items,
            "{{RANGE_PERCENTAGE}}": str(range_pct),
            "{{YEAR_LOW}}": f"${range_52w_low:.2f}",
            "{{YEAR_HIGH}}": f"${range_52w_high:.2f}",
            "{{TECHNICAL_TABLE_ROWS}}": technical_rows,
            "{{ENTRY_ZONE}}": f"${price*0.97:.2f} - ${price*0.99:.2f}",
            "{{STOP_LOSS}}": f"${price*0.94:.2f}",
            "{{TARGET_ITEMS}}": target_items,
            "{{TARGET_WALL}}": f"<div class='stat-item'><div class='stat-label'>Institutional 12M</div><div class='stat-value'>${price*1.2:.2f}</div></div>",
            "{{RAW_PRICE}}": str(price),
            "{{RAW_STOP}}": str(price*0.94),
            "{{TICKER}}": ticker,
            "{{DISCLOSURE_TEXT}}": f"Bunny Intelligence Engine v2.0 for {ticker}. Educational use only."
        }

        report_html = self.template
        for key, val in replacements.items():
            report_html = report_html.replace(key, val)
        
        output_filename = f"report_{ticker}_{datetime.now().strftime('%Y%m%d')}.html"
        output_path = os.path.join(self.output_dir, output_filename)
        
        with open(output_path, 'w') as f:
            f.write(report_html)
            
        print(f"Generated: {output_path}")
        return output_path

if __name__ == "__main__":
    cwd = os.getcwd()
    gen = InvestorBunnyGenerator(
        template_path=os.path.join(cwd, "investor_bunny_dashboard_template.html"),
        output_dir=cwd
    )
    gen.generate_report(os.path.join(cwd, "MRVL_market_data.json"))
