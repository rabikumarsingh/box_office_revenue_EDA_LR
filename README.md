# Box Office Analysis Dashboard

An interactive web application for visualizing box office movie data.

## 🎬 Features

- **Interactive Charts**: Budget vs Revenue, Top Movies, Genre Distribution, and more
- **Real-time Statistics**: Key metrics at a glance
- **Detailed Data Table**: Complete movie information with profit/loss analysis
- **Responsive Design**: Works on desktop and mobile devices

## 📁 Project Structure

```
/workspace
├── index.html              # Main dashboard application
├── data/
│   └── movies.json         # Movie dataset
├── box_office_analysis.py  # Python analysis module
└── box-office.ipynb        # Original Jupyter notebook
```

## 🚀 Deploy to GitHub Pages

### Option 1: Using GitHub UI (Easiest)

1. **Push your code to GitHub**:
   ```bash
   git add .
   git commit -m "Add box office dashboard"
   git push origin main
   ```

2. **Enable GitHub Pages**:
   - Go to your repository on GitHub
   - Click on **Settings** → **Pages** (or **Code and automation** → **Pages**)
   - Under **Source**, select **Deploy from a branch**
   - Choose **main** branch and **/(root)** folder
   - Click **Save**

3. **Access your app**:
   - After 1-2 minutes, your site will be live at:
   - `https://yourusername.github.io/repository-name/`

### Option 2: Using GitHub CLI

```bash
# If you have gh CLI installed
gh repo create --public --source=. --push
# Then enable pages in GitHub UI as described above
```

## 🎨 Customization

### Add More Data
Edit `data/movies.json` to add more movies:

```json
{
  "movies": [
    {
      "title": "Your Movie",
      "budget": 100000000,
      "revenue": 500000000,
      "popularity": 95.5,
      "runtime": 120,
      "genre": "Action, Adventure"
    }
  ]
}
```

### Change Colors
Modify the CSS in `index.html` to customize the theme.

## 📊 Technologies Used

- **HTML5/CSS3**: Modern responsive design
- **JavaScript**: Interactive functionality
- **Plotly.js**: Professional data visualization
- **GitHub Pages**: Free static hosting

## 🌟 Demo Features

1. **Scatter Plot**: Shows relationship between budget and revenue (color = popularity)
2. **Bar Chart**: Top 10 highest-grossing movies
3. **Pie Chart**: Revenue distribution by genre
4. **Bubble Chart**: Popularity vs runtime (size = revenue, color = budget)
5. **Data Table**: Complete movie details with profit/loss indicators

## 📝 Notes

- The dashboard loads sample data from `data/movies.json`
- All visualizations are interactive - hover over points for details
- No backend required - runs entirely in the browser
- Works offline once loaded

## 🔧 Troubleshooting

If charts don't load:
- Ensure `movies.json` exists in the `data` folder
- Check browser console for errors (F12)
- Verify you're accessing via HTTPS (GitHub Pages requirement)

---

Created with ❤️ for movie data enthusiasts
